// Social posts on the brand dashboards (product spec G1–G4, E, F6, F7, D; tech spec flow 12):
//   Posts for review („Постове за преглед“)          one row per pack or fix PR; a pack opens a panel
//                                                     with every post as its network shows it and the
//                                                     checks; approving is the merge of its PR in GitHub
//   Scheduled & published („Насрочени и публикувани“) one row per post; Post now, Cancel, Not before, Fix
//   New post („Нов пост“)                             ask the AI for posts; the requests and commands
//                                                     and their status
//   Settings                                         a form: Save opens the issue "social: settings", which
//                                                     becomes a PR its author (or anyone of the team) merges;
//                                                     every field explains itself over its name; Stop, Lift
// Data: docs/data/social/<brand>-review.json, -schedule.json and -board.json (GitHub Pages), and for a
// public repository the open social/… PRs and their files read through the API without a key.
// The page holds no key: every action opens GitHub, where the person confirms it with their own login
// (a PR to merge or close, a file to edit, or a new issue "social: …" that social-intake.yml does).
// "publishing check not running" is computed here, from last_check_utc (older than 2 hours).
// The words on the tabs are Bulgarian or English (БГ · EN, kept in this browser).
const SocialTabs = (() => {
  const GH = SocialGitHub, MD = SocialMd, PV = SocialPreview;
  const STALE_MS = 2 * 3600 * 1000;
  const BRANDS = {
    vsichkikazina: { name: 'Всички Казина', site: 'https://vsichkikazina.bg', dir: 'VsichkiKazina', prefix: 'vk' },
    dentalvia: { name: 'DentalVia', site: 'https://www.dentalvia.de', dir: 'DentalVia', prefix: 'dv' },
  };
  const LIMIT = { facebook: 63206, instagram: 2200, x: 280, 'linkedin-page': 3000, 'linkedin-profile': 3000 };
  const NETWORK = { facebook: 'Facebook', instagram: 'Instagram', x: 'X', 'linkedin-page': 'LinkedIn Page',
                    'linkedin-profile': 'LinkedIn profile' };
  const BADGE_CLASS = { 'Published': 'ok', 'Scheduled': 'ok', 'Planned': 'info', 'Waiting for article': 'info',
                        'Held': 'warn', 'Needs fix': 'warn', 'Article changed': 'warn', 'Failed': 'bad',
                        'Expired': 'mute', 'Cancelled': 'mute', 'Rejected': 'mute', 'Not from a pack': 'bad' };
  const ACCOUNT_FIELDS = [['active', 'Active'], ['postiz_channel_id', 'Postiz channel'], ['slots', 'Slots (local time)'],
                          ['posts_per_article', 'Posts per article'], ['followup_delay_days', 'Follow-up after (days)'],
                          ['max_per_day', 'Max a day'], ['format', 'Format'], ['slides', 'Slides in a carousel'],
                          ['link', 'Link'], ['max_hashtags', 'Max hashtags'], ['emoji', 'Emoji'],
                          ['tone_override', 'Tone (instead of the brand\'s)'],
                          ['test_post_seen', 'Test post seen (date, who)'], ['profile_link_set', 'Profile link set']];
  // settings.py ACCOUNT_DEFAULTS and BRAND_DEFAULTS: what an empty cell or a missing row means
  const ACCOUNT_DEFAULT = { active: 'off', posts_per_article: '1', followup_delay_days: '14', format: 'auto', slides: '5',
                            link: 'in post', slots: 'daily 12:30, 19:30', max_per_day: '2', emoji: 'light' };
  const BRAND_DEFAULT = { social: 'off', pause: 'off', time_zone: 'Europe/Sofia', language: 'bg',
                          eligible_types: 'guide, comparison, review, news', allowed_link_areas: '/blog/',
                          image_budget_usd: '60', packs_per_run: '5', analytics_source: 'ahrefs', art: 'every slide' };
  // the brand's keys in the Settings form, and the input of a field: on/off, choices, a number, a long text or a line
  const BRAND_FIELDS = [['social', 'onoff'], ['pause', 'onoff'], ['language', 'text'], ['time_zone', 'text'],
                        ['voice_notes', 'long'], ['compliance_long', 'long'], ['compliance_short', 'text'],
                        ['eligible_types', 'text'], ['allowed_link_areas', 'text'], ['address_pattern', 'text'],
                        ['brand_hashtags', 'text'], ['image_budget_usd', 'number'], ['packs_per_run', 'number'],
                        ['art', ['every slide', 'cover']], ['operator_names_manual', 'long'], ['offer_words', 'long'],
                        ['register_words', 'long'], ['allowed_number_names', 'long'], ['analytics_source', 'text'],
                        ['identities_verified', 'text']];
  const FIELD_KIND = { active: 'onoff', format: ['single', 'carousel', 'auto'], link: ['in post', 'profile', 'none'],
                       emoji: ['light', 'none'], slides: 'number', posts_per_article: 'number', followup_delay_days: 'number',
                       max_per_day: 'number', max_hashtags: 'number' };
  // what a field means, shown while the mouse is over its name or the field is being edited: [English, Bulgarian]
  const HELP = {
    social: ['The main switch. on: the AI writes posts for this brand and they go out. off: nothing is written or published. It can be on only once "identities verified" is filled in.',
             'Главният ключ. да: AI пише постове за марката и те се публикуват. не: нищо не се пише и не излиза. Може да е „да“ само когато „профилите проверени“ е попълнено.'],
    pause: ['on: nothing goes out. At the next check (minute :10) the posts already handed to Postiz are pulled back and wait; with off they are planned again. To stop within 5 minutes, use "Stop now" above.',
            'да: нищо не излиза. При следващата проверка (в :10) постовете, вече подадени към Postiz, се връщат и чакат; с „не“ се планират отново. За спиране до 5 минути използвай „Спри веднага“ горе.'],
    language: ['The language of the posts (bg = Bulgarian).', 'Езикът на постовете (bg = български).'],
    time_zone: ['The time zone of every hour in these settings (the posting hours, "Not before"). Europe/Sofia is Bulgarian time.',
                'Часовата зона на всички часове тук (часовете за публикуване, „Не преди“). Europe/Sofia е българско време.'],
    voice_notes: ['Notes for the AI on how the brand sounds: tone, how it addresses people, what it avoids.',
                  'Указания към AI как звучи марката: тон, обръщение, какво избягва.'],
    compliance_long: ['The responsible gambling line (18+) that ends every post, word for word. A post without it fails the checks.',
                      'Редът за отговорна игра (18+), с който завършва всеки пост, дума по дума. Пост без него не минава проверките.'],
    compliance_short: ['A shorter line for X, where a post has 280 characters. Empty: the long line is used.',
                       'По-кратък ред за X, където постът е до 280 знака. Празно: ползва се дългият.'],
    eligible_types: ['The kinds of articles the AI takes by itself: guide, comparison, review, news. It does not take other kinds.',
                     'Видовете статии, за които AI пише постове сам: guide (ръководство), comparison (сравнение), review (ревю), news (новина). Други видове не взима сам.'],
    allowed_link_areas: ['The parts of the site a post may link to, e.g. /blog/. A link anywhere else fails the checks; operator and bonus pages never pass.',
                         'Частите на сайта, към които пост може да сочи, напр. /blog/. Линк другаде не минава проверките; страниците на оператори и бонуси никога.'],
    address_pattern: ['How an article\'s address is made: {slug} becomes the article\'s short name. It must stay on the brand\'s site.',
                      'Как се образува адресът на статия: {slug} се заменя с краткото име на статията. Трябва да е в сайта на марката.'],
    brand_hashtags: ['Hashtags that go in every post of the brand. They count toward each network\'s hashtag limit. Empty: none.',
                     'Хаштагове, които влизат във всеки пост на марката. Броят се в лимита за хаштагове на всяка мрежа. Празно: никакви.'],
    image_budget_usd: ['The most the AI pictures (Gemini) may cost in a month, in dollars. Once it is spent, posts get simpler pictures without AI until the month ends.',
                       'Колко най-много могат да струват AI снимките (Gemini) за месец, в долари. Щом се похарчи, до края на месеца постовете получават по-прости снимки без AI.'],
    packs_per_run: ['How many new articles or requests the AI takes in one writing run (1–20). The rest wait for the next run.',
                    'Колко нови статии или поръчки AI взима на едно писане (1–20). Останалите чакат следващото.'],
    art: ['every slide: each slide of a carousel gets its own AI picture. cover: only the first slide does; the others are text on the brand\'s colours, which is cheaper.',
          'на всеки слайд: всеки слайд на карусела има своя AI снимка. само на корицата: снимка има само първият слайд, останалите са текст в цветовете на марката (по-евтино).'],
    operator_names_manual: ['Operator (casino) names a post must never mention, on top of the ones the system finds on the site by itself. Separate them with commas.',
                            'Имена на оператори (казина), които пост никога не споменава, освен тези, които системата сама намира в сайта. Разделяй ги със запетая.'],
    offer_words: ['Words for bonuses and offers. A post may not put an amount next to them (e.g. "100 лв бонус"), and an article with one next to an amount in its title gets no posts.',
                  'Думи за бонуси и оферти. Пост не може да има сума до тях (напр. „бонус 100 лв“), а статия със сума до такава дума в заглавието не получава постове.'],
    register_words: ['Words that invite people to sign up or deposit, e.g. "регистрирайте се". A post with one of them fails the checks.',
                     'Думи, които подканват към регистрация или депозит, напр. „регистрирайте се“. Пост с такава дума не минава проверките.'],
    allowed_number_names: ['Names with a number in them, e.g. the game "20 Super Hot". Every number in a post must come from a source; these names do not count as numbers.',
                           'Имена с число в тях, напр. играта „20 Super Hot“. Всяко число в пост трябва да идва от източник; тези имена не се броят за числа.'],
    analytics_source: ['Where the traffic data comes from (ahrefs). For reference only: nothing uses it yet.',
                       'Откъде идват данните за трафика (ahrefs). Само за справка: засега нищо не го използва.'],
    identities_verified: ['The date and who checked everyone with access to the repository (people, keys, apps). Until it is filled in, "social" cannot be on.',
                          'Дата и кой е проверил всички с достъп до хранилището (хора, ключове, приложения). Докато е празно, „постове“ не може да е „да“.'],
    active: ['on: this profile gets posts. It can be on only after its test post was seen and the Postiz channel is set (Instagram also needs the link in the profile).',
             'да: този профил получава постове. Може да е „да“ само след видян тестов пост и зададен канал в Postiz (Instagram иска и линк в профила).'],
    postiz_channel_id: ['The ID of this profile\'s channel in Postiz, the tool that publishes. Copy it from Postiz.',
                        'Номерът (ID) на канала на профила в Postiz, инструмента, който публикува. Копира се от Postiz.'],
    slots: ['The hours posts go out, in the brand\'s time zone. E.g. "daily 12:30, 19:30" (every day) or "mon-fri 10:00; sat 11:00" (Monday to Friday, and Saturday).',
            'В кои часове излизат постовете, по часовата зона на марката. Напр. „daily 12:30, 19:30“ (всеки ден) или „mon-fri 10:00; sat 11:00“ (понеделник–петък и събота).'],
    posts_per_article: ['How many posts one article gets on this profile (1–5). Each one after the first is a follow-up with another angle.',
                        'Колко поста получава една статия в този профил (1–5). Всеки след първия е допълнителен пост с друг ъгъл.'],
    followup_delay_days: ['How many days after the previous post of the same article the next one may go out.',
                          'След колко дни от предишния пост за същата статия може да излезе следващият.'],
    max_per_day: ['The most posts this profile publishes in one day.', 'Най-много постове на ден в този профил.'],
    format: ['carousel: several slides (a cover, the points, a closing slide). single: one picture. auto: a carousel when the article has enough points, otherwise one picture.',
             'Карусел: няколко слайда (корица, точки, последен слайд). Една снимка: пост с една снимка. Автоматично: карусел, когато статията има достатъчно точки, иначе една снимка.'],
    slides: ['How many slides a carousel has, 3–10: the cover, the points and the closing slide.',
             'Колко слайда има каруселът, 3–10: корица, точки и последен слайд.'],
    link: ['in post: the post carries the link to the article. profile: the post says "The link is in our profile" (Instagram allows no links in posts). none: no link.',
           'в поста: постът съдържа линк към статията. в профила: постът казва „Линкът е в профила ни.“ (Instagram не позволява линкове в постове). без: без линк.'],
    max_hashtags: ['The most hashtags in a post, not counting the brand\'s; together they stay within the network\'s limit. Empty: the network\'s limit.',
                   'Най-много хаштагове в пост, без тези на марката; заедно с тях не надхвърлят лимита на мрежата. Празно: лимитът на мрежата.'],
    emoji: ['light: at most 2 emoji in a post. none: no emoji.', 'малко: до 2 емоджи в пост. без: никакви емоджи.'],
    tone_override: ['A different tone for this profile only, instead of the brand\'s voice notes. Empty: the brand\'s.',
                    'Друг тон само за този профил, вместо указанията за тон на марката. Празно: тези на марката.'],
    test_post_seen: ['When and who saw this profile\'s test post live, e.g. "2026-10-22, name". Needed before the profile can be active.',
                     'Кога и кой е видял тестовия пост на живо, напр. „2026-10-22, име“. Нужно е, преди профилът да се включи.'],
    profile_link_set: ['Instagram: the date and who put the site\'s link in the profile. Needed before Instagram can be active.',
                       'За Instagram: дата и кой е сложил линка към сайта в профила. Нужно е, преди Instagram да се включи.'],
  };
  // the fields without which posts do not go out (settings.py's errors, links.py's link areas): [when, English, Bulgarian];
  // when: 'on' (a switch that must be on), 'always', 'social' (while the brand is on), 'active' (while the account is on)
  const REQUIRED = {
    social: ['on', 'Required: on, or nothing goes out.', 'Задължително „да“, иначе нищо не излиза.'],
    compliance_long: ['always', 'Required: empty stops every post of the brand.', 'Задължително: празно спира всички постове на марката.'],
    eligible_types: ['always', 'Required: empty stops every post of the brand.', 'Задължително: празно спира всички постове на марката.'],
    allowed_link_areas: ['always', 'Required: empty, and no post with a link passes the checks.',
                         'Задължително: празно и никой пост с линк не минава проверките.'],
    identities_verified: ['social', 'Required while social is on: empty stops every post of the brand.',
                          'Задължително, щом „постове“ е „да“: празно спира всички постове на марката.'],
    active: ['on', 'Required: on, or this profile gets no posts.', 'Задължително „да“, иначе профилът не получава постове.'],
    postiz_channel_id: ['active', 'Required while the profile is active: empty, and it gets no posts.',
                        'Задължително, щом профилът е включен: празно и той не получава постове.'],
    test_post_seen: ['active', 'Required while the profile is active: empty, and it gets no posts.',
                     'Задължително, щом профилът е включен: празно и той не получава постове.'],
    profile_link_set: ['active', 'Required while the profile is active: empty, and it gets no posts.',      // Instagram only
                       'Задължително, щом профилът е включен: празно и той не получава постове.'],
  };
  let tick = 0, freshSchedule = null, livePRs = null, brandKey = 'vsichkikazina', dataBase = './data/social';
  const filters = { state: '', network: '', account_id: '' };
  const ui = { sel: null, selPr: null, pack: null, loading: {}, cmd: null, msg: null, dirty: false, board: null };

  // --- the language of the tabs ----------------------------------------------------------------------
  const LANG_KEY = 'px-social-lang';
  const lang = () => { try { return localStorage.getItem(LANG_KEY) === 'en' ? 'en' : 'bg'; } catch (e) { return 'bg'; } };
  const BG = {
    // tabs, the bar, messages
    'Posts for review': 'Постове за преглед', 'Scheduled & published': 'Насрочени и публикувани', 'New post': 'Нов пост',
    'Social settings': 'Настройки', 'dismiss': 'затвори', 'Copied.': 'Копирано.',
    'What you do here opens GitHub in a new tab, where you confirm it with your own login.':
      'Каквото правиш тук, отваря GitHub в нов таб, където го потвърждаваш със своя акаунт.',
    'Opened GitHub in a new tab: press the green "Create" there. The answer comes in that issue in about a minute.':
      'Отворих GitHub в нов таб: натисни там зеленото „Create“. Отговорът идва в същия issue след около минута.',
    'The text is long, so it is on the clipboard: paste it into the issue (Ctrl+V), then press the green "Create".':
      'Текстът е дълъг, затова е копиран: постави го в issue-то (Ctrl+V) и натисни зеленото „Create“.',
    // banners and counters
    'publishing check not running (last check {when})': 'проверката за публикуване не работи (последна: {when})',
    'publishing check not running (no check recorded yet)': 'проверката за публикуване не работи (още няма нито една)',
    'PR in review': 'PR за преглед', 'PRs in review': 'PR за преглед', 'post': 'пост', 'posts': 'поста',
    'scheduled, next 7 days': 'насрочени, следващите 7 дни', 'published this month': 'публикувани този месец', 'failed': 'неуспешни',
    'images': 'снимки', 'of': 'от',
    'Social posts are not set up for this brand yet — the tabs fill once its settings are merged and the publishing check runs.':
      'Постовете още не са настроени за тази марка: табовете се пълнят, щом настройките се одобрят и проверката тръгне.',
    // posts for review
    'No pack or fix PR waiting for review.': 'Няма постове, които чакат преглед.', 'Review': 'Преглед', 'Open in GitHub ↗': 'Отвори в GitHub ↗',
    'Status': 'Състояние', 'Source': 'Източник', 'Accounts and posts': 'Профили и постове', 'Formats': 'Формат', 'Age': 'Възраст',
    'fix PR': 'поправка', 'in review': 'за преглед', 'expired': 'изтекъл', 'redo requested': 'поискано пренаписване',
    'waiting long': 'чака отдавна', 'opened since the last data rebuild': 'отворен след последното обновяване',
    'Requests that failed': 'Неуспешни заявки', 'Skipped (operator or bonus articles)': 'Пропуснати (статии за оператори или бонуси)',
    '← All packs': '← Всички', 'Loading {what}…': 'Зареждам {what}…', '✓ all checks pass': '✓ всички проверки минават',
    '✗ some checks fail': '✗ има непреминали проверки', 'checks running…': 'проверките вървят…', 'no checks yet': 'още няма проверки',
    'approved (merged)': 'одобрен', 'rejected (closed)': 'отхвърлен', 'refresh': 'обнови',
    'Approve: Merge in GitHub ↗': 'Одобри: Merge в GitHub ↗',
    'Reject: Close in GitHub ↗': 'Откажи: Close в GitHub ↗',
    'This page cannot read the PR (a private repository, or GitHub\'s limit for pages): open it in GitHub.':
      'Таблото не може да прочете PR-а (частно хранилище или лимитът на GitHub): отвори го в GitHub.',
    'What to fix': 'Какво да се поправи', '{pid}: deleted in this PR (it leaves the pack)': '{pid}: изтрит (не е част от пакета)',
    'Edit in GitHub ↗': 'Редактирай в GitHub ↗', 'Ask for a rewrite': 'Поискай пренаписване',
    'Write in the PR, as a comment:': 'Напиши в PR-а като коментар:', 'copy': 'копирай', 'Open the PR ↗': 'Отвори PR-а ↗',
    // scheduled & published
    'all': 'всички', 'Network': 'Мрежа', 'Account': 'Профил', 'last check {when}': 'последна проверка {when}',
    'No posts here yet.': 'Още няма постове.', 'Post': 'Пост', 'Article or request': 'Статия или заявка', 'Time (local)': 'Час (местен)',
    'Links': 'Връзки', 'Actions': 'Действия', 'post ↗': 'пост ↗', 'article ↗': 'статия ↗', 'missing on the page': 'липсва на страницата',
    'Post now': 'Публикувай веднага', 'Cancel': 'Отмени', 'Not before…': 'Не преди…', 'Fix': 'Поправи', 'Move': 'Премести', 'cancel': 'отказ',
    'Schedule for…': 'Насрочи за…', 'Schedule ↗': 'Насрочи ↗', 'When should it go out?': 'Кога да излезе?',
    'In the first free slot': 'В първия свободен час', 'about {when}': 'около {when}', '(just Merge)': '(само Merge)',
    'At once after the merge ↗': 'Веднага след Merge ↗', 'At a day and time:': 'В ден и час:',
    'For 2 or 3: press the green "Create" in GitHub, then Merge (the choice waits for the merge). Merge is the approval: anyone with write access to the repository can give it.':
      'За 2 или 3: натисни зеленото „Create“ в GitHub, после Merge (изборът чака Merge-а). Merge е одобрението: може всеки с право на запис в хранилището.',
    'The time has passed: choose a later one.': 'Този час мина: избери по-късен.',
    'Published': 'Публикуван', 'Scheduled': 'Насрочен', 'Planned': 'Планиран', 'Waiting for article': 'Чака статията',
    'Held': 'Задържан', 'Needs fix': 'Нужна е поправка', 'Article changed': 'Статията е променена', 'Failed': 'Неуспешен',
    'Expired': 'Изтекъл', 'Cancelled': 'Отменен', 'Rejected': 'Отхвърлен', 'Not from a pack': 'Не е от системата',
    // new post: ask the AI
    'Ask the AI for posts': 'Помоли AI да напише постове', 'Continue in GitHub ↗': 'Продължи в GitHub ↗',
    '(not switched on)': '(не е включен)',
    'The AI writes posts by itself from every approved article. Here you can ask it for more: an older article, a keyword or a free topic. They come to "Posts for review".':
      'AI пише постове сам от всяка одобрена статия. Тук можеш да му поръчаш още: за по-стара статия, ключова дума или свободна тема. Идват в „Постове за преглед“.',
    'About': 'За какво', 'an article (older or not yet posted)': 'статия', 'a keyword': 'ключова дума',
    'a free topic': 'свободна тема', 'a section intro': 'въведение на раздел',
    'Article': 'Статия', 'Section': 'Раздел', 'Keyword or topic': 'Ключова дума или тема',
    'not on the site yet': 'още не е на сайта', 'Loading the articles…': 'Зареждам статиите…',
    'Angle (optional)': 'Ъгъл и тон (по желание)', 'e.g. myth vs fact, a light tone': 'напр. мит или факт, лек тон',
    'More options': 'Още настройки', 'Format': 'Формат', 'carousel': 'Карусел', 'single': 'Една снимка',
    'Slides (for a carousel)': 'Брой слайдове (за карусел)', 'auto': 'Автоматично',
    'Slides in a carousel': 'Слайдове в карусела', 'Earliest date (optional)': 'Не по-рано от (по желание)',
    'Page of ours to link to (keyword or topic, optional)': 'Наша страница за линка (по желание)',
    'Sources (keyword or topic, optional): one web address per line, or paste a text. The posts may take facts from them; each fact is checked word for word.':
      'Източници (по желание): по един уеб адрес на ред или поставен текст. Постовете могат да вземат факти от тях; всеки факт се проверява дума по дума.',
    'or the text itself': 'или самия текст', 'Accounts (none ticked = every active account):': 'Профили (нищо отметнато = всички включени):',
    'Write the article, keyword or topic.': 'Избери статия или напиши ключова дума или тема.',
    'Sources are for a keyword or a free topic; an article or an intro has its own text.':
      'Източници са за ключова дума или свободна тема; статията има свой текст.',
    // settings
    'Publishing': 'Публикуване', 'Stop now': 'Спри веднага', 'Lift a stop': 'Пусни отново',
    'To stop every post of the brand within 5 minutes, write this as a comment on the "Social control" issue; anyone with write access lifts it, the same way:':
      'За да спреш всички постове на марката до 5 минути, напиши това като коментар в issue-то „Social control“; всеки с право на запис пуска отново, по същия начин:',
    'Open "Social control" ↗': 'Отвори „Social control“ ↗', 'Brand': 'Марка', 'Accounts': 'Профили',
    'Change any field and press "Save in GitHub". GitHub opens with your change: press "Create". In about a minute the issue links a PR: Merge it (anyone with write access may, you too) and the publishing check applies it at its next run (minute :10).':
      'Промени което поле искаш и натисни „Запази в GitHub“. GitHub се отваря с промяната: натисни „Create“. След около минута в issue-то идва линк към PR: натисни Merge (може всеки с право на запис, и ти) и проверката я прилага при следващото си минаване (в :10).',
    'Changes waiting for a Merge ↗': 'Промени, които чакат Merge ↗', 'Save in GitHub ↗': 'Запази в GitHub ↗',
    'Undo my changes': 'Върни както беше', 'Nothing has changed yet.': 'Още нищо не е променено.',
    'Required: without it posts do not go out. In red: missing now. Hold the mouse over a name to see what it does.':
      'Задължително: без него постовете не излизат. В червено: липсва сега. Задръж мишката върху име, за да видиш какво прави.',
    'missing': 'липсва',
    'Settings change': 'Промяна на настройките', '(empty)': '(празно)',
    'Opened GitHub in a new tab: press the green "Create" there. In about a minute the issue gets a link to a PR with your change: Merge it there and the change counts.':
      'Отворих GitHub в нов таб: натисни там зеленото „Create“. След около минута в issue-то идва линк към PR с промяната: натисни Merge там и тя влиза в сила.',
    'Active': 'Включен', 'Postiz channel': 'Канал в Postiz', 'Slots (local time)': 'Часове (местно време)', 'Posts per article': 'Постове на статия',
    'Follow-up after (days)': 'Втори пост след (дни)', 'Max a day': 'Най-много на ден', 'Link': 'Линк', 'Max hashtags': 'Най-много хаштагове',
    'Emoji': 'Емоджи', 'Test post seen (date, who)': 'Видян тестов пост (дата, кой)', 'Profile link set': 'Линк в профила',
    'Tone (instead of the brand\'s)': 'Тон (вместо този на марката)',
    'social': 'постове', 'pause': 'пауза', 'time zone': 'часова зона', 'language': 'език',
    'voice notes': 'тон и стил (указания към AI)', 'brand hashtags': 'хаштагове на марката', 'art': 'снимки в карусела',
    'every slide': 'на всеки слайд', 'cover': 'само на корицата', 'operator names manual': 'имена на оператори (ръчно)',
    'offer words': 'забранени думи: оферти', 'register words': 'забранени думи: регистрация',
    'allowed number names': 'позволени имена с числа', 'analytics source': 'източник на анализи',
    'Settings errors': 'Грешки в настройките', 'on': 'да', 'off': 'не',
    'compliance long': 'ред за отговорна игра', 'compliance short': 'кратък ред (за X)', 'eligible types': 'видове статии',
    'allowed link areas': 'разрешени части на сайта', 'address pattern': 'адрес на статия', 'image budget usd': 'бюджет за снимки ($ на месец)',
    'packs per run': 'пакета на едно писане', 'identities verified': 'профилите проверени', 'in post': 'в поста', 'profile': 'в профила',
    'light': 'малко', 'none': 'без',
  };
  function t(s, v) {
    let out = (lang() === 'bg' && BG[s]) || s;
    if (v) out = out.replace(/\{(\w+)\}/g, (m, k) => (v[k] != null ? v[k] : m));
    return out;
  }
  const TAB_LABELS = { 'social-review': 'Posts for review', 'social-schedule': 'Scheduled & published',
                       'social-requests': 'New post', 'social-settings': 'Social settings' };
  const tabLabel = key => t(TAB_LABELS[key] || key);

  const esc = v => String(v == null ? '' : v).replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const B = () => BRANDS[brandKey] || BRANDS.vsichkikazina;
  const social = () => `${B().dir}/social`;
  const when = iso => new Date(iso).toLocaleString(lang() === 'bg' ? 'bg-BG' : 'en-GB', { dateStyle: 'medium', timeStyle: 'short' });
  const ext = (href, label, cls) => `<a class="${cls || 'sc-btn'}" href="${esc(href)}" target="_blank" rel="noopener">${label}</a>`;
  const issueLink = (title, label, body) => ext(GH.newIssueUrl(title, body || issueNote()), label, 'sc-link');
  const issueNote = () => lang() === 'bg'
    ? 'Натисни зеленото **Create**. GitHub Action го изпълнява и отговаря тук след около минута.'
    : 'Press the green **Create**. A GitHub Action does it and answers here in about a minute.';

  // --- data ------------------------------------------------------------------------------------------
  async function pages(url) {
    const resp = await fetch(url + '?_=' + Date.now());
    if (!resp.ok) throw new Error('HTTP ' + resp.status);
    return resp.json();
  }

  async function apiSchedule(brand) {
    try {
      const f = await GH.getFile(`docs/data/social/${brand}-schedule.json`, 'main');
      return JSON.parse(f.text);
    } catch (e) { return null; }                       // a private repository, or the limit: the Pages copy is used
  }

  async function apiPRs(prefix) {
    try {
      const arr = await GH.pulls('open');
      if (!Array.isArray(arr)) return null;
      return arr.filter(p => ((p.head && p.head.ref) || '').startsWith(`social/${prefix}/`)).map(p => ({
        pack_id: p.head.ref.split('/').pop(), number: p.number, url: p.html_url, title: p.title,
        created: p.created_at, labels: (p.labels || []).map(l => l.name) }));
    } catch (e) { return null; }
  }

  // brand: vsichkikazina | dentalvia; prefix: vk | dv; base: the folder of the JSON files
  async function load(brand, prefix, base) {
    brandKey = brand;
    dataBase = base;
    tick++;
    const out = { brand, review: null, schedule: null, prs: livePRs, missing: false };
    try { out.review = await pages(`${base}/${brand}-review.json`); } catch (e) { out.missing = true; }
    try { out.schedule = await pages(`${base}/${brand}-schedule.json`); } catch (e) { out.missing = true; }
    try { ui.board = await pages(`${base}/${brand}-board.json`); } catch (e) { ui.board = ui.board || null; }
    // the API answers a public repository without a key, 60 times an hour: fresh copies now and then
    if (tick % 4 === 1) freshSchedule = (await apiSchedule(brand)) || freshSchedule;
    if (tick % 4 === 3 || livePRs === null) livePRs = (await apiPRs(prefix)) || livePRs || [];
    if (freshSchedule && (!out.schedule || (freshSchedule.generated_utc || '') >= (out.schedule.generated_utc || ''))) {
      out.schedule = freshSchedule;
      out.missing = !out.review && !out.schedule;
    }
    out.prs = livePRs;
    out.reviewRows = reviewRows(out);
    out.scheduleRows = (out.schedule && out.schedule.rows) || [];
    out.openRequests = ((out.review && out.review.open_requests) || []).length;
    return out;
  }

  // G1: open pack and fix PRs (registry rows, plus PRs opened since the last rebuild), expired fix PRs
  function reviewRows(st) {
    const rows = ((st.review && st.review.rows) || []).filter(r => ['in review', 'expired'].includes(r.status));
    const known = new Set(rows.map(r => r.pack_id));
    for (const p of st.prs || []) {
      const row = rows.find(r => r.pr === p.number);
      if (row) { row.labels = p.labels; continue; }
      if (known.has(p.pack_id)) continue;
      const fix = /-fix-\d+$/.test(p.pack_id);
      rows.push({ pack_id: p.pack_id, kind: fix ? 'fix' : 'pack', source: p.pack_id.replace(/-p\d+(-fix-\d+)?$/, ''),
                  title: p.title, accounts: [], posts: null, formats: [], pr: p.number, pr_url: p.url,
                  status: 'in review', created: (p.created || '').slice(0, 10), age_days: null, labels: p.labels,
                  note: 'opened since the last data rebuild' });
    }
    return rows;
  }

  const settingsOf = () => (ui.board && ui.board.settings) || { brand: {}, accounts: [], errors: [] };
  const brandSettings = () => settingsOf().brand || {};

  // a pack as its PR holds it now: the copy the PR workflow keeps for the dashboard (no key, any
  // repository), else read through the API (a public repository)
  async function loadPack(packId, number) {
    if (ui.loading.pack) return;
    ui.loading.pack = true;
    let out;
    try { out = await previewPack(packId, number); } catch (e) { out = await apiPack(packId, number); }
    ui.pack = out;
    ui.loading.pack = false;
  }

  // docs/data/social/previews/<pack id>/ (preview_export.py): the posts, pack.json, the checks, the images
  async function previewPack(packId, number) {
    const dir = `${dataBase}/previews/${encodeURIComponent(packId)}`;
    const data = await pages(`${dir}/preview.json`);
    if (number && data.pr && data.pr.number && +data.pr.number !== +number) throw new Error('the preview is of another PR');
    const v = encodeURIComponent((data.pr && data.pr.head && data.pr.head.sha) || '');
    const images = {}, posts = {};
    for (const [pid, files] of Object.entries(data.images || {})) images[pid] = files.map(f => `${dir}/${encodeURIComponent(f)}?v=${v}`);
    for (const [pid, post] of Object.entries(data.posts || {})) posts[pid] = { fields: post.fields };
    return { id: packId, number, pr: data.pr, branch: data.pr.head.ref, dir: `${social()}/packs/${packId.replace(/-fix-\d+$/, '')}`,
             meta: data.meta, posts, images, checks: data.checks, fixes: data.fixes || [] };
  }

  async function apiPack(packId, number) {
    const out = { id: packId, number };
    try {
      out.pr = await GH.pull(number);
      const ref = out.pr.head.sha;
      out.branch = out.pr.head.ref;
      out.dir = `${social()}/packs/${packId.replace(/-fix-\d+$/, '')}`;
      out.meta = JSON.parse((await GH.getFile(`${out.dir}/pack.json`, ref)).text);
      out.posts = {};
      for (const post of out.meta.posts || []) {
        try {
          const f = await GH.getFile(`${out.dir}/posts/${post.post_id}.md`, ref);
          out.posts[post.post_id] = { raw: f.text, fields: MD.parsePost(f.text) };
        } catch (e) { out.posts[post.post_id] = null; }          // deleted in this PR: it leaves the pack
      }
      out.images = {};
      for (const post of out.meta.posts || []) {
        out.images[post.post_id] = await Promise.all((post.visuals || []).map(v =>
          GH.imageUrl(`${out.dir}/visuals/${v.file}`, ref).catch(() => '')));
      }
      const status = await GH.combinedStatus(ref).catch(() => null);
      const sc = status && (status.statuses || []).find(s => s.context === 'social-checks');
      out.checks = sc ? { state: sc.state, text: sc.description } : null;
      const comments = await GH.comments(number).catch(() => []);
      const sticky = (comments || []).find(c => (c.body || '').includes('<!-- social-checks -->'));
      out.fixes = sticky ? whatToFix(sticky.body) : [];
    } catch (e) { out.error = e.message; }
    return out;
  }

  function whatToFix(body) {
    const lines = body.split('\n');
    const at = lines.findIndex(l => l.trim() === '**What to fix**');
    if (at < 0) return [];
    const out = [];
    for (const l of lines.slice(at + 1)) {
      if (l.startsWith('- ')) out.push(l.slice(2).replace(/`/g, ''));
      else if (out.length && !l.trim()) break;
    }
    return out;
  }

  // the preview data of one post (preview.py builds the same for the offline page)
  function postView(pack, post, fields) {
    const net = post.network;
    let text = MD.publishText(fields);
    const link = post.link || {};
    let address = null, tag = null;
    if (link.mode === 'placeholder') {
      address = MD.expectedAddress(pack.meta, post, { site: B().site, address_pattern: brandSettings().address_pattern });
      if (address) tag = MD.tagged(address, net, link.campaign, link.content || post.post_id);
    }
    const length = MD.length(text, net, tag ? tag.length : null);
    if (tag) text = text.split(MD.LINK).join(tag);
    const id = post.account_id || '';
    return { post_id: post.post_id, network: net, account_id: id, handle: id.includes('-') ? id.split('-').slice(1).join('-') : id,
             name: B().name, format: post.format || 'single', text, images: (pack.images[post.post_id] || []).filter(Boolean),
             image_text: fields.image_text || [], alt: fields.alt_text || '', hashtags: fields.hashtags || [],
             link: address, link_note: link.mode !== 'placeholder' ? (link.reason || '') : '', length, limit: LIMIT[net] };
  }

  // --- shared pieces ---------------------------------------------------------------------------------
  function banners(st) {
    const out = [...((st.schedule && st.schedule.banners) || [])];
    const last = st.schedule && st.schedule.last_check_utc;
    const on = st.schedule && st.schedule.brand_state && st.schedule.brand_state.social;
    if (last && Date.now() - new Date(last) > STALE_MS)
      out.unshift({ kind: 'check', level: 'red', text: t('publishing check not running (last check {when})', { when: new Date(last).toLocaleString('en-GB') }) });
    else if (!last && on === 'on')
      out.unshift({ kind: 'check', level: 'red', text: t('publishing check not running (no check recorded yet)') });
    return out;
  }

  function bannerHtml(st) {
    const list = banners(st);
    if (!list.length) return '';
    return '<div class="sc-banners">' + list.map(b =>
      `<div class="sc-banner sc-${b.level === 'red' ? 'red' : b.level === 'info' ? 'info' : 'warn'}">${esc(b.text)}</div>`).join('') + '</div>';
  }

  function countersHtml(st) {
    const c = (st.schedule && st.schedule.counters) || {};
    const spend = st.schedule && st.schedule.image_spend;
    const posts = n => `${n || 0} ${t(n === 1 ? 'post' : 'posts')}`;
    const items = [[`${c.in_review || 0}`, t(c.in_review === 1 ? 'PR in review' : 'PRs in review') +
                    (c.in_review_posts ? ` (${posts(c.in_review_posts)})` : '')],
                   [`${c.scheduled_next_7_days || 0}`, t('scheduled, next 7 days')],
                   [`${c.published_this_month || 0}`, t('published this month')],
                   [`${c.failed || 0}`, t('failed'), c.failed ? 'bad' : '']];
    let html = '<div class="sc-counters">' + items.map(([n, l, cls]) =>
      `<span class="sc-counter ${cls || ''}"><b>${n}</b> ${esc(l)}</span>`).join('');
    if (spend) html += `<span class="sc-counter">${t('images')} <b>$${spend.usd}</b> ${t('of')} $${spend.budget_usd} (${esc(spend.month)})</span>`;
    const bs = st.schedule && st.schedule.brand_state;
    if (bs && bs.badges && bs.badges.length) html += bs.badges.map(b => `<span class="sc-counter bad"><b>${esc(b)}</b></span>`).join('');
    return html + '</div>';
  }

  function notSetUp(st) {
    if (!st.missing) return '';
    return `<div class="empty">${t('Social posts are not set up for this brand yet — the tabs fill once its settings are merged and the publishing check runs.')}</div>`;
  }

  function msgHtml() {
    if (!ui.msg) return '';
    return `<div class="sc-msg sc-msg-${ui.msg.kind}">${esc(ui.msg.text)} <button class="sc-link" data-sc="dismiss">${t('dismiss')}</button></div>`;
  }

  const langSwitch = () => `<span class="sc-lang">${[['bg', 'БГ'], ['en', 'EN']].map(([k, l]) =>
    `<button class="sc-link${lang() === k ? ' sc-on' : ''}" data-sc="lang" data-lang="${k}">${l}</button>`).join(' · ')}</span>`;

  // the bar over every tab: how acting works, the language, the last message
  function topBar() {
    let html = `<div class="sc-auth"><span class="hint">${t('What you do here opens GitHub in a new tab, where you confirm it with your own login.')}</span>`;
    if (GH.LOCAL && GH.REPO !== 'ProfitXtraV2/AIContent') html += ` <span class="sc-badge sc-warn">${esc(GH.REPO)}</span>`;
    return html + langSwitch() + '</div>' + msgHtml();
  }
  const copyButton = text => `<code class="sc-code">${esc(text)}</code> <button class="sc-link" data-sc="copy" data-text="${esc(text)}">${t('copy')}</button>`;

  // --- Posts for review ----------------------------------------------------------------------------------
  function renderReview(st) {
    if (ui.sel) return topBar() + packPanel();
    if (st.missing && !st.reviewRows.length) return topBar() + bannerHtml(st) + notSetUp(st);
    const rows = st.reviewRows;
    let html = topBar() + bannerHtml(st) + countersHtml(st);
    if (!rows.length) html += `<div class="empty">${t('No pack or fix PR waiting for review.')}</div>`;
    else {
      const body = rows.map(r => {
        const status = [r.kind === 'fix' ? 'fix PR' : '', r.status, ...(r.labels || []).filter(l => l === 'redo requested'),
                        r.waiting_long ? 'waiting long' : ''].filter(Boolean);
        const open = r.pr && r.status === 'in review'
          ? `<button class="sc-btn sc-primary" data-sc="open" data-pack="${esc(r.pack_id)}" data-pr="${+r.pr}">${t('Review')}</button> ` +
            ext(GH.prUrl(r.pr), t('Open in GitHub ↗'), 'sc-link') : '';
        return `<tr><td>${status.map(s => `<span class="st st-${s === 'expired' ? 'failed' : 'drafted'}">${esc(t(s))}</span>`).join(' ')}</td>` +
          `<td><b>${esc(r.source)}</b> ${esc(r.title)}${r.note ? `<br><span class="hint">${esc(t(r.note))}</span>` : ''}</td>` +
          `<td>${[esc((r.accounts || []).join(', ')), r.posts != null ? `${r.posts} ${t(r.posts === 1 ? 'post' : 'posts')}` : '']
                 .filter(Boolean).join(' · ') || '—'}</td>` +
          `<td>${esc((r.formats || []).map(f => t(f)).join(', ')) || '—'}</td>` +
          `<td>${r.pr ? ext(GH.prUrl(r.pr), `#${+r.pr}`, 'sc-link') : '—'}</td>` +
          `<td class="num">${r.age_days != null ? r.age_days + ' d' : esc(r.created)}</td><td>${open}</td></tr>`;
      }).join('');
      html += `<table><thead><tr><th>${t('Status')}</th><th>${t('Source')}</th><th>${t('Accounts and posts')}</th><th>${t('Formats')}</th><th>PR</th><th>${t('Age')}</th><th></th></tr></thead><tbody>${body}</tbody></table>`;
    }
    const failed = (st.review && st.review.failed_requests) || [];
    const skipped = (st.review && st.review.skipped) || [];
    if (failed.length)
      html += `<h3>${t('Requests that failed')}</h3><ul class="sc-list">` + failed.map(f =>
        `<li><b>${esc(f.id)}</b> ${esc(f.kind)} ${esc(f.target)} — ${esc(f.reason)}</li>`).join('') + '</ul>';
    if (skipped.length)
      html += `<h3>${t('Skipped (operator or bonus articles)')}</h3><ul class="sc-list">` + skipped.map(s =>
        `<li><b>${esc(s.item_id)}</b> — ${esc(s.reason)}</li>`).join('') + '</ul>';
    return html;
  }

  function packPanel() {
    const p = ui.pack;
    const back = `<button class="sc-btn" data-sc="close">${t('← All packs')}</button>`;
    const prLink = ext(GH.prUrl(ui.selPr), t('Open the PR ↗'), 'sc-btn sc-primary');
    if (!p || p.id !== ui.sel) return `<div class="sc-panel">${back} <span class="hint">${esc(t('Loading {what}…', { what: ui.sel }))}</span></div>`;
    if (p.error) return `<div class="sc-panel">${back} ${prLink}<p class="hint">${t('This page cannot read the PR (a private repository, or GitHub\'s limit for pages): open it in GitHub.')}</p></div>`;
    const open = p.pr.state === 'open';
    const checks = p.checks ? p.checks.state : null;
    const chip = checks === 'success' ? `<span class="sc-badge sc-ok">${t('✓ all checks pass')}</span>`
      : checks === 'failure' ? `<span class="sc-badge sc-bad">${t('✗ some checks fail')}</span>`
      : checks === 'pending' ? `<span class="sc-badge sc-info">${t('checks running…')}</span>`
      : `<span class="sc-badge sc-mute">${t('no checks yet')}</span>`;
    const state = open ? '' : `<span class="sc-badge ${p.pr.merged ? 'sc-ok' : 'sc-mute'}">${t(p.pr.merged ? 'approved (merged)' : 'rejected (closed)')}</span>`;
    let html = `<div class="sc-panel"><div class="sc-panel-head">${back}
      <div class="sc-panel-title"><b>${esc(p.id)}</b> · ${esc(p.pr.title)} · ${ext(GH.prUrl(p.number), `PR #${+p.number} ↗`, 'sc-link')}</div>
      <div class="sc-panel-acts">${chip} ${state}
        ${open ? ext(GH.prUrl(p.number), t('Approve: Merge in GitHub ↗'), 'sc-btn sc-primary') + ' ' +
                 ext(GH.prUrl(p.number), t('Reject: Close in GitHub ↗'), 'sc-btn sc-danger') : ''}
        <button class="sc-link" data-sc="reload-pack">${t('refresh')}</button></div></div>`;
    if (open) html += whenBlock(p);
    if (p.fixes.length) html += `<div class="sc-banner sc-warn"><b>${t('What to fix')}</b><ul>` + p.fixes.map(f => `<li>${esc(f)}</li>`).join('') + '</ul></div>';
    html += '<div class="sc-posts">';
    for (const post of p.meta.posts || []) {
      const file = p.posts[post.post_id];
      if (!file) { html += `<div class="sc-post"><p class="hint">${esc(t('{pid}: deleted in this PR (it leaves the pack)', { pid: post.post_id }))}</p></div>`; continue; }
      const acts = open ? ext(GH.editUrl(p.branch, `${p.dir}/posts/${post.post_id}.md`), t('Edit in GitHub ↗')) +
        ` <span class="hint">${t('Ask for a rewrite')}: ${t('Write in the PR, as a comment:')}</span> ${copyButton(`/redo ${post.post_id} `)}` : '';
      html += `<div class="sc-post"><div class="sc-preview" data-post="${esc(post.post_id)}"></div><div class="sc-post-acts">${acts}</div></div>`;
    }
    return html + '</div></div>';
  }

  // the next slot of the given accounts from now + 30 minutes (planner.py LEAD), in this browser's time;
  // the publishing check also counts the posts already planned, so it is "about"
  function nextSlot(accountIds) {
    const from = new Date(Date.now() + 30 * 60000);
    let best = null;
    for (const a of (settingsOf().accounts || []).filter(x => accountIds.includes(x.account_id))) {
      let rules;
      try { rules = MD.parseSlots(a.slots); } catch (e) { continue; }
      for (let d = 0; d < 8; d++) {
        const day = new Date(from.getFullYear(), from.getMonth(), from.getDate() + d);
        const weekday = (day.getDay() + 6) % 7;              // 0 = Monday, as settings.py counts
        for (const rule of rules) if (rule.days.includes(weekday)) for (const tm of rule.times) {
          const [h, m] = tm.split(':').map(Number);
          const at = new Date(day.getFullYear(), day.getMonth(), day.getDate(), h, m);
          if (at >= from && (!best || at < best)) best = at;
        }
      }
    }
    return best;
  }

  // when the approved posts go out: chosen before the merge (a post now or post at line waits for it)
  function whenBlock(p) {
    const accounts = [...new Set((p.meta.posts || []).map(x => x.account_id))];
    const slot = nextSlot(accounts);
    return `<div class="sc-when"><b>${t('When should it go out?')}</b>
      <div class="sc-when-opts">
        <div>1. ${t('In the first free slot')}: <b>${slot ? esc(t('about {when}', { when: when(slot.toISOString()) })) : '—'}</b>
          <span class="hint">${t('(just Merge)')}</span></div>
        <div>2. ${issueLink(`social: post now ${p.id}`, t('At once after the merge ↗'))}</div>
        <form class="sc-inline" data-sc-form="postat" data-target="${esc(p.id)}">3. ${t('At a day and time:')}
          <input type="datetime-local" name="at" required> <button class="sc-btn" type="submit">${t('Schedule ↗')}</button></form>
      </div>
      <p class="hint">${esc(t('For 2 or 3: press the green "Create" in GitHub, then Merge (the choice waits for the merge). Merge is the approval: anyone with write access to the repository can give it.'))}</p></div>`;
  }

  function fillPreviews(root) {
    const p = ui.pack;
    if (!p || !p.meta) return;
    root.querySelectorAll('.sc-preview[data-post]').forEach(box => {
      const pid = box.getAttribute('data-post');
      const post = (p.meta.posts || []).find(x => x.post_id === pid);
      const file = p.posts[pid];
      if (!post || !file) return;
      box.textContent = '';
      box.appendChild(PV.slot(postView(p, post, file.fields)));
    });
  }

  // --- Scheduled & published ---------------------------------------------------------------------------
  function options(rows, key, label, fmt) {
    const values = [...new Set(rows.map(r => r[key]).filter(Boolean))].sort();
    return `<label>${label} <select data-sc-filter="${key}"><option value="">${t('all')}</option>` +
      values.map(v => `<option value="${esc(v)}"${filters[key] === v ? ' selected' : ''}>${esc(fmt ? fmt(v) : v)}</option>`).join('') +
      '</select></label>';
  }

  const NOT_IN_TOOL = ['Waiting for article', 'Planned', 'Held'];
  function rowActions(r) {
    const b = (kind, label, ok) => ok ? issueLink(`social: ${kind} ${r.post_id}`, t(label)) : '';
    if (ui.cmd && ui.cmd.post === r.post_id && ui.cmd.kind === 'at')
      return `<form class="sc-inline" data-sc-form="postat" data-target="${esc(r.post_id)}"><input type="datetime-local" name="at" required>
        <button class="sc-btn sc-primary" type="submit">${t('Schedule ↗')}</button><button class="sc-link" type="button" data-sc="cmd-cancel">${t('cancel')}</button></form>`;
    if (ui.cmd && ui.cmd.post === r.post_id)
      return `<form class="sc-inline" data-sc-form="notbefore" data-post="${esc(r.post_id)}"><input type="date" name="date" required>
        <button class="sc-btn sc-primary" type="submit">${t('Move')}</button><button class="sc-link" type="button" data-sc="cmd-cancel">${t('cancel')}</button></form>`;
    const live = ['Planned', 'Scheduled', 'Waiting for article'].includes(r.badge);
    const notBefore = NOT_IN_TOOL.includes(r.badge)
      ? `<button class="sc-link" data-sc="notbefore" data-post="${esc(r.post_id)}">${t('Not before…')}</button>` : '';
    const at = live ? `<button class="sc-link" data-sc="postat" data-post="${esc(r.post_id)}">${t('Schedule for…')}</button>` : '';
    return [b('post now', 'Post now', live), at, b('cancel', 'Cancel', NOT_IN_TOOL.includes(r.badge)), notBefore,
            b('fix', 'Fix', [...NOT_IN_TOOL, 'Failed'].includes(r.badge))].filter(Boolean).join(' · ');
  }

  function renderSchedule(st) {
    if (st.missing && !st.scheduleRows.length) return topBar() + bannerHtml(st) + notSetUp(st);
    const head = topBar() + bannerHtml(st) + countersHtml(st);
    const all = st.scheduleRows;
    const rows = all.filter(r => (!filters.state || r.badge === filters.state) &&
      (!filters.network || r.network === filters.network) && (!filters.account_id || r.account_id === filters.account_id));
    const tz = (st.schedule && st.schedule.time_zone) || '';
    let html = head + '<div class="sc-filters">' + options(all.map(r => ({ ...r, state: r.badge })), 'state', t('Status'), v => t(v)) +
      options(all, 'network', t('Network'), v => NETWORK[v] || v) + options(all, 'account_id', t('Account')) +
      (st.schedule && st.schedule.last_check_utc ? `<span class="hint">${esc(t('last check {when}', { when: new Date(st.schedule.last_check_utc).toLocaleString('en-GB') }))}</span>` : '') +
      '</div>';
    if (!rows.length) return html + `<div class="empty">${t('No posts here yet.')}</div>`;
    const body = rows.map(r => {
      const reason = ['Waiting for article', 'Held', 'Needs fix', 'Article changed', 'Failed'].includes(r.badge) && r.reason_text
        ? `: ${esc(r.reason_text)}` : '';
      const missing = (r.missing_lines || []).length ? `<br><span class="hint">${t('missing on the page')}: ${r.missing_lines.map(esc).join(' · ')}</span>` : '';
      const marks = (r.markers || []).map(m => `<span class="sc-mark">${esc(m)}</span>`).join(' ');
      const links = [r.network_url ? `<a href="${esc(r.network_url)}" target="_blank" rel="noopener">${t('post ↗')}</a>` : '',
                     r.article_url ? `<a href="${esc(r.article_url)}" target="_blank" rel="noopener">${t('article ↗')}</a>` : ''].filter(Boolean).join(' ');
      return `<tr><td><span class="sc-badge sc-${BADGE_CLASS[r.badge] || 'info'}">${esc(t(r.badge))}</span>${reason}${missing}${marks ? '<br>' + marks : ''}</td>` +
        `<td><code>${esc(r.post_id)}</code></td><td>${esc(NETWORK[r.network] || r.network)}<br><span class="hint">${esc(r.account_id)}</span></td>` +
        `<td>${esc(r.source || r.pack_id)} ${esc(r.title)}</td><td class="num">${esc(r.time_local)}${r.time_local && tz ? `<br><span class="hint">${esc(tz)}</span>` : ''}</td>` +
        `<td>${links || '—'}</td><td>${rowActions(r)}</td></tr>`;
    }).join('');
    return html + `<table><thead><tr><th>${t('Status')}</th><th>${t('Post')}</th><th>${t('Network')}</th><th>${t('Article or request')}</th><th>${t('Time (local)')}</th><th>${t('Links')}</th><th>${t('Actions')}</th></tr></thead><tbody>${body}</tbody></table>`;
  }

  // --- New post: ask the AI, and the requests and commands -----------------------------------------------
  const accountsOf = () => settingsOf().accounts || [];
  const accountLabel = a => `${NETWORK[a.network] || a.network}`;

  function renderAsk() {
    const accounts = accountsOf();
    // the articles a request may name: approved or on the site, not about an operator or a bonus; newest first
    const lib = ((ui.board && ui.board.library) || []).filter(i => ['approved', 'posted'].includes(i.board_status) && !i.operator_or_bonus)
      .sort((a, b) => (b.id || '').localeCompare(a.id || ''));
    const option = i => `<option value="${esc(i.id)}">${esc(i.id)} · ${esc(i.title || i.slug)}${i.live ? '' : ` (${t('not on the site yet')})`}</option>`;
    const articles = lib.filter(i => i.kind !== 'hub-intro'), intros = lib.filter(i => i.kind === 'hub-intro');
    return `<form class="sc-form sc-request" data-sc-form="request">
        <p class="hint">${t('The AI writes posts by itself from every approved article. Here you can ask it for more: an older article, a keyword or a free topic. They come to "Posts for review".')}</p>
        <div class="sc-grid">
          <label>${t('About')}<select name="kind"><option value="article">${t('an article (older or not yet posted)')}</option>
            <option value="keyword">${t('a keyword')}</option><option value="topic">${t('a free topic')}</option>
            <option value="intro">${t('a section intro')}</option></select></label>
          <label class="sc-target" data-kinds="article">${t('Article')}<select name="target-article">${articles.length
            ? articles.map(option).join('') : `<option value="">${t('Loading the articles…')}</option>`}</select></label>
          <label class="sc-target" data-kinds="intro" hidden>${t('Section')}<select name="target-intro">${intros.map(option).join('')}</select></label>
          <label class="sc-target" data-kinds="keyword topic" hidden>${t('Keyword or topic')}<input name="target-text" placeholder="бакара стратегия · 7 грешки при рулетката"></label>
          <label>${t('Angle (optional)')}<input name="angle" placeholder="${esc(t('e.g. myth vs fact, a light tone'))}"></label>
        </div>
        <details class="sc-more"><summary>${t('More options')}</summary><div class="sc-form">
        <div class="sc-grid">
          <label>${t('Format')}<select name="format"><option value="carousel" selected>${t('carousel')}</option><option value="single">${t('single')}</option></select></label>
          <label>${t('Slides (for a carousel)')}<select name="slides">${[3, 4, 5, 6, 7, 8, 9, 10].map(n => `<option${n === 5 ? ' selected' : ''}>${n}</option>`).join('')}</select></label>
          <label>${t('Earliest date (optional)')}<input type="date" name="earliest"></label>
          <label>${t('Page of ours to link to (keyword or topic, optional)')}<input name="target_page" placeholder="https://vsichkikazina.bg/blog/…/"></label>
        </div>
        <label>${t('Sources (keyword or topic, optional): one web address per line, or paste a text. The posts may take facts from them; each fact is checked word for word.')}
          <textarea name="sources" rows="4" placeholder="https://…&#10;${esc(t('or the text itself'))}"></textarea></label>
        <div class="sc-checks"><span class="hint">${t('Accounts (none ticked = every active account):')}</span>
          ${accounts.map(a => `<label class="sc-check"><input type="checkbox" name="accounts" value="${esc(a.account_id)}"> ${esc(accountLabel(a))}${a.active === 'on' ? '' : ` <span class="hint">${t('(not switched on)')}</span>`}</label>`).join('')}</div>
        </div></details>
        <button class="sc-btn sc-primary" type="submit">${t('Continue in GitHub ↗')}</button></form>`;
  }

  function renderRequests() {
    return topBar() +
      `<section class="sc-section"><h3>${t('Ask the AI for posts')}</h3>${renderAsk()}</section>`;
  }

  // the issue intake.py turns into a request row (a pasted source text saved under sources/)
  async function continueRequest(form) {
    const val = n => ((form.querySelector(`[name="${n}"]`) || {}).value || '').trim();
    const kind = val('kind');
    const target = val(['article', 'intro'].includes(kind) ? `target-${kind}` : 'target-text');
    if (!target) { say('err', t('Write the article, keyword or topic.')); refresh(); return; }
    const lines = val('sources').split('\n').map(l => l.trim());
    const urls = lines.filter(l => /^https?:\/\/\S+$/.test(l));
    const pasted = lines.filter(l => !/^https?:\/\/\S+$/.test(l)).join('\n').trim();
    if ((urls.length || pasted) && !['keyword', 'topic'].includes(kind)) {
      say('err', t('Sources are for a keyword or a free topic; an article or an intro has its own text.'));
      refresh();
      return;
    }
    const data = { brand: brandKey, kind, target, angle: val('angle'), format: val('format'), slides: val('slides'),
                   earliest: val('earliest'), target_page: val('target_page'), sources: urls,
                   accounts: [...form.querySelectorAll('[name="accounts"]:checked')].map(i => i.value) };
    const body = `<!-- social:request ${JSON.stringify(data)} -->\n**${t('About')}:** ${t({ article: 'an article (older or not yet posted)', keyword: 'a keyword', topic: 'a free topic', intro: 'a section intro' }[kind] || kind)}: ${target}\n\n` +
      (pasted ? `<!-- source -->\n${pasted}\n<!-- /source -->\n\n` : '') + issueNote() + '\n';
    const got = await GH.openIssue(`social: request ${target}`.slice(0, 120), body);
    say('ok', got.copied ? t('The text is long, so it is on the clipboard: paste it into the issue (Ctrl+V), then press the green "Create".')
                         : t('Opened GitHub in a new tab: press the green "Create" there. The answer comes in that issue in about a minute.'));
    ui.dirty = false;
    refresh();
  }

  // --- Settings: a form; Save opens the issue "social: settings", which intake.py makes a PR to merge ------
  const onOff = v => (['on', 'yes', 'true'].includes(String(v || '').trim().toLowerCase()) ? 'on' : 'off');
  const cellText = v => String(v == null ? '' : v).replace(/\s+/g, ' ').replace(/\|/g, '/').trim();   // mdtable.clean

  // one field; data-initial holds the value as the file has it, so Save sends only what changed; req: its REQUIRED entry
  function settingField(name, kind, value, label, key, req) {
    const initial = kind === 'onoff' ? onOff(value) : cellText(value);
    const attrs = `name="${esc(name)}" data-initial="${esc(initial)}"`;
    let input;
    if (kind === 'onoff' || Array.isArray(kind)) {
      const choices = kind === 'onoff' ? ['on', 'off'] : (kind.includes(initial) ? kind : [initial, ...kind]);
      input = `<select ${attrs}>${choices.map(c => `<option value="${esc(c)}"${c === initial ? ' selected' : ''}>${esc(t(c))}</option>`).join('')}</select>`;
    } else if (kind === 'long') input = `<textarea ${attrs} rows="2">${esc(initial)}</textarea>`;
    else input = `<input ${attrs} value="${esc(initial)}"${kind === 'number' ? ' inputmode="decimal"' : ''}>`;
    const bg = lang() === 'bg' ? 1 : 0;
    const tip = (req ? `<b>${esc(req[bg + 1])}</b> ` : '') + esc(HELP[key] ? HELP[key][bg] : '');
    const cap = `<span class="sc-cap">${esc(label)}${req ? '<span class="sc-req" aria-hidden="true">*</span>' : ''}` +
      ` <span class="sc-help" aria-hidden="true">?</span><span class="sc-tip" role="tooltip">${tip}</span>` +
      `<span class="sc-miss-note">${t('missing')}</span></span>`;
    return `<label${kind === 'long' ? ' class="sc-wide"' : ''}${req ? ` data-req="${req[0]}"` : ''}>${cap}${input}</label>`;
  }

  // red: a required field that is empty while it counts (always, or while the brand or its account is on)
  function markMissing(form) {
    const on = name => { const el = form.querySelector(`[name="${name}"]`); return !!el && el.value === 'on'; };
    for (const label of form.querySelectorAll('label[data-req]')) {
      const el = label.querySelector('[data-initial]'), when = label.getAttribute('data-req');
      const counts = when === 'always' || (when === 'social' && on('b:social')) ||
                     (when === 'active' && on(`a:${el.name.split(':')[1]}:active`));
      label.classList.toggle('sc-missing', counts && !el.value.trim());
    }
  }

  function renderSettings(st) {
    let html = topBar();
    const s = settingsOf();
    const brand = s.brand || {};
    const bs = (st && st.schedule && st.schedule.brand_state) || {};
    html += `<div class="sc-stop"><div><b>${t('Publishing')}</b>: ${t('social')} ${esc(t(onOff(brand.social)))}${(bs.badges || []).length ? ' · ' + bs.badges.map(b => `<span class="sc-badge sc-bad">${esc(b)}</span>`).join(' ') : ''}</div>
      <div><span class="hint">${esc(t('To stop every post of the brand within 5 minutes, write this as a comment on the "Social control" issue; anyone with write access lifts it, the same way:'))}</span></div>
      <div>${t('Stop now')}: ${copyButton(`/stop-now ${brandKey}`)} · ${t('Lift a stop')}: ${copyButton(`/lift ${brandKey}`)}
        ${ext(GH.issuesUrl('is:issue is:open in:title "Social control"'), t('Open "Social control" ↗'), 'sc-btn')}</div></div>`;
    if ((s.errors || []).length) html += `<div class="sc-banner sc-red"><b>${t('Settings errors')}</b><ul>${s.errors.map(e => `<li>${esc(e.message || e)}</li>`).join('')}</ul></div>`;
    html += `<p class="hint">${esc(t('Change any field and press "Save in GitHub". GitHub opens with your change: press "Create". In about a minute the issue links a PR: Merge it (anyone with write access may, you too) and the publishing check applies it at its next run (minute :10).'))}
      ${ext(GH.pullsUrl('is:pr is:open in:title "social: settings"'), t('Changes waiting for a Merge ↗'), 'sc-link')}</p>`;
    html += `<form class="sc-form sc-settings" data-sc-form="settings">` +
      `<p class="hint"><span class="sc-req">*</span> ${esc(t('Required: without it posts do not go out. In red: missing now. Hold the mouse over a name to see what it does.'))}</p>` +
      `<h3>${t('Brand')}</h3><div class="sc-grid">` +
      BRAND_FIELDS.map(([k, kind]) => settingField(`b:${k}`, kind, k in brand ? brand[k] : BRAND_DEFAULT[k], t(k.replace(/_/g, ' ')), k, REQUIRED[k])).join('') +
      `</div><h3>${t('Accounts')}</h3>`;
    for (const a of s.accounts || []) {
      html += `<fieldset class="sc-account"><legend>${esc(NETWORK[a.network] || a.network)} <span class="hint">${esc(a.account_id)}</span></legend><div class="sc-grid">` +
        ACCOUNT_FIELDS.filter(([k]) => k !== 'slides' || ['facebook', 'instagram'].includes(a.network))   // only they post carousels
          .map(([k, label]) => settingField(`a:${a.account_id}:${k}`, FIELD_KIND[k] || 'text', a[k] || ACCOUNT_DEFAULT[k], t(label), k,
                                            k === 'profile_link_set' && a.network !== 'instagram' ? null : REQUIRED[k])).join('') +
        '</div></fieldset>';
    }
    return html + `<div class="sc-inline"><button class="sc-btn sc-primary" type="submit">${t('Save in GitHub ↗')}</button>
      <button class="sc-btn" type="button" data-sc="settings-reset">${t('Undo my changes')}</button></div></form>`;
  }

  // the fields that differ from the file, as the issue intake.py turns into a PR
  async function saveSettings(form) {
    const brandChanges = {}, accountChanges = {}, lines = [];
    for (const el of form.querySelectorAll('[data-initial]')) {
      const value = cellText(el.value);
      if (value === el.getAttribute('data-initial')) continue;
      const [scope, id, key] = el.name.split(':');
      if (scope === 'b') brandChanges[id] = value;
      else (accountChanges[id] = accountChanges[id] || {})[key] = value;
      lines.push(`- ${scope === 'b' ? id : `${id} · ${key}`}: ${value || t('(empty)')}`);
    }
    if (!lines.length) { say('err', t('Nothing has changed yet.')); refresh(); return; }
    const data = { brand: brandKey, brand_changes: brandChanges, account_changes: accountChanges };
    const note = lang() === 'bg'
      ? 'Натисни зеленото **Create**. След около минута GitHub Action отговаря тук с линк към PR с промяната: натисни **Merge** в него, за да влезе в сила.'
      : 'Press the green **Create**. In about a minute a GitHub Action answers here with a link to a PR that holds the change: **Merge** it to apply it.';
    const body = `<!-- social:settings ${JSON.stringify(data).replace(/-->/g, '--\\u003e')} -->\n**${t('Settings change')}:**\n${lines.join('\n')}\n\n${note}\n`;
    const got = await GH.openIssue(`social: settings ${brandKey}`, body);
    say('ok', got.copied ? t('The text is long, so it is on the clipboard: paste it into the issue (Ctrl+V), then press the green "Create".')
                         : t('Opened GitHub in a new tab: press the green "Create" there. In about a minute the issue gets a link to a PR with your change: Merge it there and the change counts.'));
    ui.dirty = false;
    refresh();
  }

  // --- actions ------------------------------------------------------------------------------------------
  function say(kind, text) { ui.msg = { kind, text }; }
  function refresh() { if (window.__activate && window.__tabKey) window.__activate(window.__tabKey); }

  // one listener for every button and form of the tabs (links open GitHub by themselves)
  function onClick(ev) {
    const el = ev.target.closest('[data-sc]');
    if (!el || el.disabled) return;
    const what = el.getAttribute('data-sc');
    const post = el.getAttribute('data-post');
    switch (what) {
      case 'dismiss': ui.msg = null; refresh(); break;
      case 'lang':
        try { localStorage.setItem(LANG_KEY, el.getAttribute('data-lang')); } catch (e) { /* private window */ }
        location.reload();                                // the page's own tab names follow
        break;
      case 'copy':
        navigator.clipboard.writeText(el.getAttribute('data-text')).then(() => { say('ok', t('Copied.')); refresh(); }, () => {});
        break;
      case 'open': ui.sel = el.getAttribute('data-pack'); ui.selPr = +el.getAttribute('data-pr'); ui.pack = null; ui.msg = null; refresh(); break;
      case 'close': ui.sel = null; ui.pack = null; ui.msg = null; refresh(); break;
      case 'reload-pack': ui.pack = null; refresh(); break;
      case 'notbefore': ui.cmd = { post }; refresh(); break;
      case 'postat': ui.cmd = { post, kind: 'at' }; refresh(); break;
      case 'cmd-cancel': ui.cmd = null; refresh(); break;
      case 'settings-reset': ui.dirty = false; ui.msg = null; refresh(); break;
      default: break;
    }
  }

  function onSubmit(ev) {
    const form = ev.target.closest('[data-sc-form]');
    if (!form) return;
    ev.preventDefault();
    const kind = form.getAttribute('data-sc-form');
    if (kind === 'notbefore') {
      const pid = form.getAttribute('data-post'), date = form.querySelector('[name="date"]').value;
      GH.openIssue(`social: not before ${pid} ${date}`, issueNote());
      say('ok', t('Opened GitHub in a new tab: press the green "Create" there. The answer comes in that issue in about a minute.'));
      ui.cmd = null; refresh();
    } else if (kind === 'postat') {                          // a post or a whole pack, at a local day and time
      const target = form.getAttribute('data-target'), at = form.querySelector('[name="at"]').value;
      if (!at || new Date(at) < new Date(Date.now() + 60 * 1000)) { say('err', t('The time has passed: choose a later one.')); refresh(); return; }
      GH.openIssue(`social: post at ${target} ${at.replace('T', ' ')}`, issueNote());
      say('ok', t('Opened GitHub in a new tab: press the green "Create" there. The answer comes in that issue in about a minute.'));
      ui.cmd = null; refresh();
    } else if (kind === 'request') continueRequest(form);
    else if (kind === 'settings') saveSettings(form);
  }

  function onInput(ev) {
    const form = ev.target.closest('[data-sc-form]');
    if (!form) {
      const f = ev.target.closest('[data-sc-filter]');
      if (f) { filters[f.getAttribute('data-sc-filter')] = f.value; refresh(); }
      return;
    }
    ui.dirty = true;
    if (form.getAttribute('data-sc-form') === 'settings') markMissing(form);
    if (form.getAttribute('data-sc-form') === 'request' && ev.target.name === 'kind')      // an article, a section, or words
      form.querySelectorAll('.sc-target').forEach(l => { l.hidden = !l.getAttribute('data-kinds').split(' ').includes(ev.target.value); });
  }

  let listening = false;
  // called by the page after it puts a social tab's HTML in place: wires events, fills previews, loads data
  function mount(root, kind) {
    if (!listening) {
      document.addEventListener('click', onClick);
      document.addEventListener('submit', onSubmit);
      document.addEventListener('input', onInput);
      document.addEventListener('change', ev => {
        if (ev.target.closest('[data-sc-filter]')) onInput(ev);
      });
      listening = true;
    }
    if (ui.lastKind && ui.lastKind !== kind && ui.msg) {        // a message belongs to the tab it was made on
      ui.msg = null;
      const m = root.querySelector('.sc-msg');
      if (m) m.remove();
    }
    ui.lastKind = kind;
    const settingsForm = root.querySelector('[data-sc-form="settings"]');
    if (settingsForm) markMissing(settingsForm);
    if (kind === 'social-review') {
      if (ui.sel && (!ui.pack || ui.pack.id !== ui.sel) && !ui.loading.pack) loadPack(ui.sel, ui.selPr).then(refresh);
      fillPreviews(root);
    }
  }

  // true while a panel or a form is open: the page's 90-second refresh leaves it alone
  const isBusy = () => !!(ui.sel || ui.cmd || ui.dirty);

  // the tabs' own styles, added once (the pages keep their own stylesheet as it is)
  (function css() {
    const el = document.createElement('style');
    el.textContent = `
      .sc-banners { display: grid; gap: .35rem; margin: .2rem 0 .8rem; }
      .sc-banner { padding: .45rem .7rem; border-radius: 8px; font-size: .86rem; border: 1px solid; margin: .3rem 0; }
      .sc-banner ul { margin: .3rem 0 0 1.1rem; padding: 0; }
      .sc-red { background: #fdecec; border-color: #f3b4b4; color: #8a1c1c; font-weight: 600; }
      .sc-warn { background: #fff6e5; border-color: #f2d49b; color: #7a4b00; }
      .sc-info { background: #eef4fd; border-color: #c4d8f5; color: #1f4f8f; }
      .sc-counters { display: flex; flex-wrap: wrap; gap: .4rem; margin: 0 0 .8rem; }
      .sc-counter { background: #f1f4f9; border-radius: 999px; padding: .2rem .65rem; font-size: .82rem; }
      .sc-counter.bad { background: #fdecec; color: #a11d1d; }
      .sc-filters { display: flex; flex-wrap: wrap; gap: .8rem; align-items: center; margin: 0 0 .7rem; font-size: .84rem; }
      .sc-badge { display: inline-block; padding: .1rem .5rem; border-radius: 6px; font-size: .78rem; font-weight: 600; border: 0; }
      .sc-ok { background: #e3f5ea; color: #0f6b3a; } .sc-info { background: #eef4fd; color: #1f4f8f; }
      .sc-warn { background: #fff1d6; color: #7a4b00; } .sc-bad { background: #fdecec; color: #a11d1d; }
      .sc-mute { background: #eef0f3; color: #5b6472; }
      .sc-mark { display: inline-block; font-size: .72rem; color: #5b6472; border: 1px solid #d9dee6; border-radius: 6px;
                 padding: 0 .35rem; margin-top: .2rem; }
      .sc-list { margin: .3rem 0 1rem 1.1rem; font-size: .86rem; }
      .sc-btn { font: inherit; font-size: .84rem; padding: .3rem .75rem; border-radius: 8px; border: 1px solid #cfd6e0;
                background: #fff; color: #14161a; cursor: pointer; text-decoration: none; display: inline-block; }
      .sc-btn:hover:not([disabled]) { border-color: #9aa6b6; }
      .sc-btn[disabled] { opacity: .5; cursor: not-allowed; }
      .sc-primary { background: #1668c7; border-color: #1668c7; color: #fff; }
      .sc-primary:hover:not([disabled]) { background: #0f57ad; }
      .sc-danger { color: #a11d1d; border-color: #f0b8b8; }
      .sc-link { font: inherit; font-size: .82rem; background: none; border: 0; padding: 0; color: #1668c7; cursor: pointer; text-decoration: underline; }
      .sc-code { background: #f1f4f9; border-radius: 6px; padding: .1rem .4rem; font-size: .82rem; }
      .sc-auth { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; margin: 0 0 .7rem; font-size: .86rem; }
      .sc-lang { margin-left: auto; } .sc-lang .sc-on { font-weight: 700; text-decoration: none; color: #14161a; }
      .sc-inline { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; }
      .sc-inline input { font: inherit; padding: .25rem .5rem; border: 1px solid #cfd6e0; border-radius: 6px; }
      .sc-msg { margin: 0 0 .8rem; padding: .45rem .7rem; border-radius: 8px; font-size: .86rem; white-space: pre-line; }
      .sc-msg-ok { background: #e3f5ea; color: #0f6b3a; } .sc-msg-err, .sc-err { background: #fdecec; color: #a11d1d; }
      .sc-msg-info { background: #eef4fd; color: #1f4f8f; } .sc-err { padding: .3rem .6rem; border-radius: 6px; }
      .sc-panel-head { display: flex; flex-wrap: wrap; gap: .6rem 1rem; align-items: center; margin-bottom: .8rem; }
      .sc-when { border: 1px solid #cfd6e0; border-radius: 8px; padding: .55rem .75rem; margin: 0 0 .8rem; font-size: .9rem; }
      .sc-when-opts { display: grid; gap: .35rem; margin: .4rem 0; }
      .sc-panel-title { flex: 1 1 320px; }
      .sc-panel-acts { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; }
      .sc-posts { display: flex; flex-wrap: wrap; gap: 28px; align-items: flex-start; margin-top: .6rem; }
      .sc-post { width: 470px; max-width: 100%; }
      .sc-post-acts { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; margin-top: .6rem; font-size: .84rem; }
      .sc-form { margin-top: .7rem; display: grid; gap: .55rem; font-size: .86rem; }
      .sc-form label { display: grid; gap: .25rem; }
      .sc-form textarea, .sc-form input, .sc-form select { font: inherit; padding: .35rem .5rem; border: 1px solid #cfd6e0; border-radius: 6px; width: 100%; box-sizing: border-box; }
      .sc-form button { justify-self: start; }
      .sc-form [hidden] { display: none !important; }
      .sc-request .sc-target { grid-column: 1 / -1; }               /* a whole row: the article titles are long */
      .sc-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: .55rem .9rem; }
      .sc-checks { display: flex; flex-wrap: wrap; gap: .4rem 1rem; align-items: center; }
      .sc-check { display: flex !important; gap: .3rem; align-items: center; }
      .sc-check input { width: auto !important; }
      .sc-section { border-top: 1px solid #e3e7ee; padding: .4rem 0 .8rem; }
      .sc-section:first-of-type { border-top: 0; }
      .sc-more > summary { cursor: pointer; padding: .3rem 0; }
      .sc-settings .sc-wide { grid-column: 1 / -1; }
      .sc-cap { position: relative; display: inline-flex; align-items: center; gap: .3rem; cursor: help; }
      .sc-help { display: inline-grid; place-items: center; width: 1rem; height: 1rem; border-radius: 50%; background: #e3e7ee; color: #4a5361; font-size: .68rem; font-weight: 700; }
      .sc-tip { display: none; position: absolute; left: 0; bottom: calc(100% + 6px); z-index: 30; width: max-content; max-width: min(340px, 80vw);
                padding: .5rem .65rem; border-radius: 8px; background: #14161a; color: #fff; font-size: .8rem; font-weight: 400; line-height: 1.4;
                box-shadow: 0 4px 14px rgba(0, 0, 0, .18); pointer-events: none; }
      .sc-cap:hover .sc-tip, .sc-settings label:focus-within .sc-tip { display: block; }   /* a phone has no hover: tapping the field shows it */
      .sc-req { color: #c0262d; font-weight: 700; margin-left: .1rem; }
      .sc-miss-note { display: none; color: #c0262d; font-size: .75rem; font-weight: 600; }
      .sc-missing .sc-miss-note { display: inline; }
      .sc-missing input, .sc-missing textarea { border-color: #d64545; background: #fff6f6; }
      .sc-account { border: 1px solid #dbdfe6; border-radius: 10px; padding: .6rem .9rem .9rem; margin: 0 0 .8rem; }
      .sc-account legend { font-weight: 600; padding: 0 .3rem; }
      .sc-stop { display: grid; gap: .5rem; background: #fff7f7; border: 1px solid #f3cccc; border-radius: 10px; padding: .7rem .9rem; margin: 0 0 1rem; }
      .sc-stop > div:last-child { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; }`;
    document.head.appendChild(el);
  })();

  return { load, renderReview, renderSchedule, renderRequests, renderSettings, mount, isBusy, banners, reviewRows, postView,
           tabLabel, t };
})();
if (typeof module !== 'undefined' && module.exports) module.exports = SocialTabs;
