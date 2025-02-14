label old_demo:
    scene bg black:

    P "Начало конца"

    scene bg saloon
    with Dissolve(.5)

    show lyokha calm at default_pos

    L "Здоров, бедолага. Не знаю, что ты там в своей Москве сделал, что тебя сюда отправили, но видно накосячил знатно. По своему желанию в нашу дыру и птицы не летают."
    
    L "Меня, кстати, Алексей зовут. Для друзей просто Лёха. Как в песне Апиной: \"Ой, Лёха, Лёха, мне без тебя так плохо\". Слышал, нет? Ты че, это ж группа \"Комбинация\"!"

    P "Слышал."

    L "Словесным поносом ты не страдаешь. Да ты не боись, сработаемся ещё."

    P "К делу."

    
    L "Ёба-боба, вот это ты Коломбо. Тогда давай я тебе вкратце опишу, что мы тут имеем. Дельце обычное, впрочем."
    
    L "Жмура в толчке нашли, прямо башкой в говно. Жак-Ив Кусто на минималках. Никто его пока не доставал, тебя ждали. Да и кто достанет – нахер он кому сдался!"
    
    L "Вокруг джином воняет, у нас походу эстета убили. Местный рядовой мужик и слова-то такого не знает."
    
    L "На попе ручки чьи-то имеются имеется, но у нас спец по дактилоскопии опять клея нанюхался, и сегодня не на работе."
    
    L "Мертвяк уже пахнуть начинает, поэтому чутка поторапливаться надо. Не розы, знаешь ли. Да и срать людям негде."
    
    L "А это для бара, дружище, проблема посерьезнее Парникового эффекта."

    P "Обычное дельце?"

    L "Да мало ли, очередной забулдыга. У нас такие дохнут как мухи на лобовухе."
    
    L "Ты сам место осмотреть пойдешь, или мне составить компанию?"

    menu:
        "Идти самому":
            jump toilet_single
        "Взять Лёху":
            jump toilet_with_L

    label toilet_single:

        scene bg atl transitions:
            "bg corridor1"
            "bg corridor2" with dissolve
            pause 0.15
            "bg corridor3" with dissolve
            pause 0.15
            "bg corridor4" with dissolve
            pause 0.15
            "bg corridor4" with dissolve
            pause 0.15
            "bg corridor1" with dissolve
            pause 0.15
            repeat
        with Dissolve(.5)

        #character per seconds value ->  {cps=25} {/cps}

        "Дерьмо..."
        "Дерьмо?"
        "Дерьмо."
        "Если бы мне в академии сказали, что я буду работать вот так, я бы лучше даже школу не заканчивал."
        "Вот Шура, как там его... Забыл фамилию. Так тот после десятого в колледж ускакал, и вроде не жалуется."
        "Или он сидит? Не помню уже ничего."
        "Не надо было в то дело лезть, совсем забыл, в какой стране родился и живу."
        "Ну порешил полковник женушку, зачем было лезть. Говорили мне в Следственном Комитете, не надо браться, самому же попадет."
        "Когда у человека много власти, он и жену убить может, и никто ему ничего не скажет. Жизнь так устроена. Сильный бьет слабого, как король бьет валета."
        "Правильно ли я поступил?"

        scene bg stairs
        with Dissolve(.5)

        "Правильно, конечно. Ублюдок должен быть наказан, вот как я считаю. Да только наказан в итоге я. Прозябаю теперь в какой-то дыре, тут даже гостиницы нет."
        "А полковнику – хоть бы хрен: ворует как воровал, блядствует как блядствовал. Хорошо хоть не замочил, в теории мог бы и это. Весь суд купил, как бублики на базаре."

        scene bg toilet
        with Dissolve(.5)

        "Головой в сортире – какая дрянь. Жизнь человек и так не выбирает, так некоторым еще и в смерти достается. Не заслужил инсульт, что ли?"

        
        P "Не лучшее место для молитвы, дружок. Хех."
        
        P "Ладно, будем обследовать."
        
        P "Ботинки изгваздал, видно, не по асфальту сюда шёл."
        
        P "Пахнет, действительно, джином. Если и пил, то явно не здесь."
        
        P "По телосложению на вид тридцатник, но при здешних условиях обитания, он мог вчера школу закончить."
        
        P "Следов крови нет, очевидно, просто утопили, без истязаний."
        
        P "Сейчас осмотрим лицо"
        
        P "Так-с, чернобровый кареокий, прямо как в песне. Действительно, лет тридцать."
        
        P "Такое ощущение, что где-то я его уже видел..."
        
        P "Да нет, показалось."
        
        P "Страшноват, конечно, но, как говорится, с лица воды не пить, так что не беда."
        
        P "А вот это что?..."
        
        P "След от удара на темечке. Похоже на тупой предмет. Вот это уже интересно. Успел все-таки по мордасам словить перед кончиной."
        
        P "Вернусь-ка я в бар, пора пройтись по свидетелям."

        scene bg saloon
        with Dissolve(.5)

        "Все на тех же местах. Разве что Алкаш уже стоит, опершись руками на стол и смотря в одну точку."

        menu:
            "Заговорить с алкашом":
                jump drunkard_branch
            "Подойти к уборщице":
                jump maiden_branch

    label drunkard_branch:
        show drunkard calm at default_pos
        
        P "Полагаю, вы в курсе произошедшего."
        Drunkard "Я то? Я в курсе, товарищ следователь."
        Drunkard "А вы?"
        
        P "Не шутите. Мне нужно знать все, что знаете вы. Вы знали убитого?"
        Drunkard "Знал. Но и вы знали убитого."
        
        P "Я сюда приехал не шарады решать, мужик. Давай лучше поговорим по-хорошему."
        Drunkard "Я говорю, как есть. Вы всё прекрасно знаете, товарищ следователь."
        
        P "Ты мне зубы не заговаривай, быстро тебя на пару суток упеку. Место в отделении найдется."
        Drunkard "Вам показалось знакомым лицо убитого, верно?"
        
        P "Откуда знаешь?"
        Drunkard "А вот знаю, и наверняка."
        
        P "Ты действуешь мне на нервы похлеще пустого бака."
        Drunkard "Не торопитесь с выводами. И рану на голове вы, я думаю, тоже заметили?"
        
        P "Да, черт возьми! Ты мне нравишься все меньше и меньше."
        Drunkard "Погодите еще минутку, детектив. Задумайтесь, не болит ли ваша голова примерно в том месте, куда ударили убитого?"
        
        P "Господи…"
        Drunkard "Это лицо – ваше, господин детектив."
        
        P "Ради всего святого!"
        Drunkard "Треньк-треньк"
        
        P "Перестань!"
        Drunkard "Треньк-треньк-треньк"
        
        P "Сию же минуту, мать твою!"
        Drunkard "ТРЕНЬК-ТРЕНЬК-ТРЕНЬК-ТРЕНЬК"

        scene bg room:
            xzoom 1.8
            yzoom 1.4


        "Черт возьми, это телефон!"
        "Перебрал вчера знатно, конечно."
        "Надо же, приснится такое."
        
        P "Алло, да, это детектив Ливанов. Про жену полковника уже слышал. Несчастная женщина. Буду ли браться за дело?..."
        "..."
        
        P "Пожалуй, нет."
        jump end_game

    label maiden_branch:
        show maiden calm at default_pos
        
        Maiden "Есть."
        
        P "Что есть?"
        
        Maiden "Прописка есть, милок, могу показать. Все справки с собой, все хорошо, все в порядке."
        
        P "Я не из миграционной службы."
        
        Maiden "Понимаю, дорогой, но, если все-таки интересно будет, я тебе все справки покажу. Я даже от кори привита."
        
        P "Да какая к черту корь! Здесь убийство произошло!"
        
        Maiden "От кори тоже умирают, дорогой, не горячись."
        
        P "Ты видела что-нибудь?"
        
        Maiden "Глазки слабые, голубчик, ничего не видела."
        
        P "Ты сегодня убиралась в туалете?"
        
        Maiden "А как же не убираться? Работа такая. И в туалете убиралась, и за стойкой, и вот столы прибрала, а ведь я не молодая уже, то спину прихватит..."
        
        P "Довольно."
        
        Maiden "Вот те крест! Не знаю я ничего. У самой проблем хватает."
        
        Maiden "Сегодня вот убиралась, ведро выронила, оно укатилось, еле отыскала."
        
        P "Минуточку…"
        
        P "Можешь показать ведро своё?"
        
        Maiden "Чего на ведро глядеть то, родной? Ведро – оно и в Африке ведро. Вот швабра у меня новая – так это просто загляденье..."
        
        P "Ведро."
        
        Maiden "Хорошо-хорошо. Вот оно. Держи."
        
        P "Ржавое какое-то, давно не меняли?"
        
        Maiden "Да как сюда устроилась, всё с одним хожу."
        
        P "Так, а вот это что?"
        
        P "Ну-ка..."
        
        P "Пятно крови на днище."
        
        P "Ты, когда ведро роняла, ничего странного не заметила?"
        
        Maiden "Упало как-то глухо, а так все в порядке было."
        
        P "Ты, дура старая, его на голову человеку уронила!"
        
        Maiden "Ой-ой. Он в порядке?"
        
        P "Не совсем – он умер."
        
        Maiden "О господи..."
        
        Maiden "Что же я наделала..."
        
        Maiden "Меня же теперь депортируют."

        jump end_game

    label toilet_with_L:

        scene bg toilet
        with Dissolve(.5)

        show lyokha calm:
            zoom 0.70
            xalign 1.0
            yalign 0.8

        
        L "Как видишь, мертвые у нас не сильно от живых отличаются"
        
        L "Тем ребятам два очка, кто лакает из бачка. Ха-ха. Ладненько, давай к делу."
        
        P "Перевернуть бы надо."
        
        L "Тут как с бабой. Надо сначала со спины осмотреть, вдруг кривая-косая, а потом уже на лицо глядеть."
        
        P "Хорошо."
        
        P "На затылке рана неглубокая, похоже, что ударили тупым предметом. Что он в таком положении здесь делал?"
        
        L "Ты, видно, не пил никогда. Или в Москве в окно блюют?"
        
        P "Действительно. Итак, наш дорогой друг преспокойно блевал в туалете, как вдруг ктото подошел к нему..."
        
        L "И дал по кочерыжке!"
        
        P "Да, по кочерыжке. У убитого были враги? Вы уже проверили его?"
        
        L "Ага, по базам данных пробили. В Интерпол звоночек сделали."
        
        P "Я серьезно"
        
        L "Как тут проверишь. У нас если паспорт человека не в конторе по микрозаймам заложен, считай, уже счастливчик. А алкашей вроде этого даже на учет не ставят."
        
        P "Прогрессивно тут у вас. Давай переворачивать."
        
        L "Кого-то мне этот тип напоминает, знакомые черты."
        
        P "У меня тоже такое чувство."
        
        L "Последний раз по карманам шарил в школе, но сейчас без этого не обойтись. Мутное дело какое-то."
        
        L "Такс, а вот и виновник торжества."
        
        L "Джин, дамы и господа. Реликвия в нашей срани, если честно."
        
        L "Опа, тут еще половина."
        
        P "Не смей, это вещественное доказательство!"
        
        L "Чем докажут? Член покажут! Ха-ха! Не волнуйся, я чутка, для обогрева мозга, так сказать."
        
        P "Дай-ка лучше бутылочку мне."
        
        P "В остальных карманах пусто, наверное, живет по соседству, раз не взял даже бумажника."
        
        L "Удивительно, здесь обычно не наливают в долг. Боря жадный, как сучка на текучке. Хорошо, что не слышал про существование чаевых. Удавил бы за них."
        
        P "Кто это?"
        
        L "Да хозяин местный, он и сейчас за стойкой торчит. Настоящий боров – палец в рот не клади."
        
        P "Поговорил бы я с ним."
        
        L "На здоровье. Тот еще урод. Я к нему подходить не стану, мне еще жить здесь. В гробу я его видал."
        
        L "Когда он пьяный на поминках туда полез."
        
        L "Как-то спокойно он ведет себя, словно засранный голубями памятник. Не нравится он мне, надо бы поговорить с ним."
        
        P "Вернемся в бар."

        L "Мне нынче совсем эта пропитая харя не нравится. Сам его допросишь, или вдвоём работать будем?"

        menu:
            "Допрашивать вместе":
                jump question_double
            "Разобраться одному":
                jump question_single

    label question_double:
        scene bg saloon
        with Dissolve(.5)

        show lyokha calm:
            xzoom -0.70
            yzoom 0.70
            xalign 0.0
            yalign 1.0

        show boris calm:
            zoom 0.70
            xalign 1.0
            yalign 1.0

        L "Боря, у тебя труп в туалете, я думаю, ты в курсе. И помер он явно не от твоей паленой водки. Что-нибудь знаешь?"
        
        Boris "Я вас, ментов, ненавижу. Чтоб вы все сдохли."
        
        P "Не стоит так говорить. Не думаю, что в тюремной кухне тебе будет приятнее работать."
        
        Boris "Я ничего не знаю. Да если бы и знал, тебе, швали, не сказал."
        
        P "Ну что же, тогда приступим к обыску."
        
        P "Здесь ничего нет..."
        
        P "Под стойкой тоже..."
        
        L "Шкаф пуст, как его черная душа."
        
        Boris "Заткнись, ублюдок!"
        
        P "А вот что-то нашлось. Папка. Это уже что-то."
        
        L "Что в папке?"
        
        Boris "Документы."
        
        P "Сейчас посмотрим."
        
        P "Так, это разрешение на продажу алкоголя... Это договор аренды... Паспорт..."
        
        P "Лёш, взгляни на паспорт!"
        
        L "Худой был, Борь, где ж ты так отожрался?"
        
        P "Да я не об этом, взгляни на лицо!"
        
        L "Вот дерьмо, да это же наш вылитый жмур!"
        
        P "Поедем в участок, или сейчас говорить начнешь?"
        
        Boris "Брат."
        
        P "Несильно ты из-за смерти брата расстроился, Борис."
        
        Boris "Мы с детства не очень дружили."
        
        L "Зато выглядели как две капли воды. Но ты еще и из-под крана был, судя по всему."
        
        Boris "Я-то тебе рожу начищу, блестеть будет."
        
        L "Это мы еще глянем, кто кому начистит."
        
        P "Больно вы похожи были с братом все-таки."
        
        Boris "Что есть, то есть, даже болели одинаково. Он, правда, чаще."

        hide boris
        show L calm:
            xalign 0.5
            yalign 1.0
        
        L "Ладно, проголодался я здесь с вами. Пока живой, надо кушать. У меня тут поесть-попить с собой, могу поделиться."
        
        P "Не откажусь."
        
        L "Жена бутерброды положила, чай, сейчас все достану."
        
        P "Вроде молодой еще, когда жениться успел?"
        
        L "У нас здесь свадьба как аэропорт: только по залёту."
        
        P "Вкусный чай, с привкусом каким-то."
        
        L "Это листья можжевельника, жена для аромата добавляет."
        
        P "Неплохо."

        show lyokha calm:
            xzoom -0.70
            yzoom 0.70
            xalign 0.0
            yalign 1.0

        show boris calm:
            zoom 0.70
            xalign 1.0
            yalign 1.0
        
        L "Борь, хоть чай будешь? Или ты безалкогольные напитки вообще не признаешь?"
        
        Boris "Не буду. Аллергия на можжевельник."
        
        L "Как знаешь."

        hide boris
        show lyokha calm:
            xalign 0.5
            yalign 1.0
        
        P "Лёша, джин."
        
        L "Всё-таки можно отпить?"
        
        P "Да нет же, джин из можжевельника делают."
        
        L "Да и пусть делают, мне то что."
        
        P "У этого борова аллергия на можжевельник, она так же могла быть у его брата, раз они, по его словам, даже болели одинаково."

        show lyokha calm:
            xzoom -0.70
            yzoom 0.70
            xalign 0.0
            yalign 1.0

        show boris calm:
            zoom 0.70
            xalign 1.0
            yalign 1.0
        
        L "Борь, а брат в содержании этой забегаловки участвовал?"
        
        Boris "Да. Она нам от отца досталась. Обоим."
        
        P "Борис, а брат в последние дни жизни не был ли простужен?"
        
        Boris "Был."
        
        P "То есть, ничего не мешало дать ему джин под видом водки, ведь он не слышал запаха..."
        
        L "Напоить и вызвать аллергическую реакцию, чтобы ослабить..."
        
        P "Дождаться, пока ему станет совсем плохо, и заставить всего одним ударом потерять сознание. Например, бить бутылкой..."
        
        L "Чтобы бар целиком перешёл в твою собственность. Да, Борь?"
        
        Boris "Суки."
        
        Boris "Гниды."
        
        P "Пакуй его, Лёш."

        jump end_game

    label question_single:

        $ flashbulb = Fade(0.2, 0.0, 0.4, color='#fff')
        hide lyokha
        show boris calm:
            zoom 0.70
            xalign 0.5
            yalign 1.0
        
        P "Борис?"
        
        Boris "Да."
        
        P "Я полагаю, вы в курсе произошедшего."
        
        Boris "Да."
        
        P "Замечательный диалог. Может быть, прокомментируете? Вы знали убитого?"
        
        Boris "Да."
        
        Boris "Не советую лезть ко мне, дружок."
        
        P "Работа у меня такая. Кем вам приходился убитый?"
        
        Boris "Брат."
        
        P "Не особо вы потерей расстроены, Борис."
        
        Boris "Не лучшие отношения были, скажем так. А вам какое дело? Отсутствие сочувствия тоже теперь преступлением является?"
        
        P "Не является. Что брат делал в вашем баре?"
        
        Boris "Он здесь работал с документами, это была его часть, я за стойкой стоял."
        
        P "Не странно ли работать вместе с братом, которого не очень любишь?"
        
        Boris "Деньги и волка с овцой заставят в мире жить. Бизнес нам по завещанию достался, выбора не было."
        
        P "Я думаю, нам надо продолжить диалог в отделении."
        
        Boris "А я так не думаю, сволочь."
        
        P "Полегче, я при исполнении."
        
        Boris "А мне плевать!"
        
        P "Что?"
        
        P "Что вы делаете?!"
        
        P "Уберите оружие!"
        
        Boris "В этом городе только один закон, детектив.{nw}"
        with flashbulb
        extend " Закон выживания."

        scene bg killer:
            xzoom 7
            yzoom 6
            xalign 0.5
            yalign 0.5
        with Dissolve(.5)
        
        Boris "Если не ты глотки рвешь, значит, рвут твою. Мы все здесь мрази. И я, и мой брат. Все."
        
        Boris "Он хотел увеличить свою долю, я был против. Если бы я его не убил, он был сделал это первым."
        
        Boris "Мы как Каин и Авель, детектив. Только мы оба Каины. Мы все здесь Каины."
        
        Boris "Мне жаль, что вы попали под руку, детектив. Боюсь, с Алексеем случится тоже самое."
        
        Boris "Он ведь только семьей обзавелся. Но не думайте, и за ним грешок найдется."
        
        P "За... за..."
        
        P "За что?"
        
        Boris "За деньги."

        return