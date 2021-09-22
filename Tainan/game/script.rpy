init:
    $ style.default.font = "msjh.ttc"
    $ style.default.language = "msjh"
init python:
   style.default.layout = "greedy"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("嚴恬",color="#26C8D1")
define b = Character("小棠",color="#26C8D1")
# define m = Character("主人公", color="#c8c8f")
define m = Character("[povname]",color="#26C8D1")

# The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

label start:
    
    scene bg 00
    window hide
    pause
    
    
    window show
    
    "有天小棠與嚴恬收到了一封匿命信，但看起來很像奇怪的惡作劇信，於是他們也就沒放心上了。"
    
    "直到有一天……"

label 光華校門口:

    play music "Pickled Pink.mp3"
    scene ch 0
    
    window hide
    pause
    
    scene bg 0
    window show

    python:
        povname = "???"

    #show cha a happy :
    #    xalign 0.2 yalign 1.0
    
    
    "……"
   
    show a happy 1 at right

    a "那照這樣的進度來看我們應該可以在下周前做完這份報告！"
    
    show b excited at left
    
    b "太好了！"

    a "對了小棠今天要來我們家一起…"
    
    hide a happy 1
    hide b excited
    
    stop music
    play sound "car-door-close-3.wav"
    
    "「咚———」"
    
    show b wow at left
    
    b "……咦咦咦？！"

    b "前面是不是發生什麼事了！" 
    
    hide b wow
    
    play sound "footsteps-2.wav"
    
    "「噠噠噠噠—」聽到奇怪的聲響後，小棠和嚴恬便加快腳步往聲音方向走去。"
    
    play music "Bass Meant Jazz.mp3" fadein 1.0
    
    show a wow at right
    
    a "有個人倒在那裡！"
    
    hide a wow
    show a 1 at right
    show b sweat at left
    
    "看到有人有困難，小棠和嚴恬便急忙跑去攙扶對方，輕輕搖醒對方。"
    
    hide a 1
    hide b sweat
    show m 1
    
    m "……"
    
    hide m 1
    show m 2
    
    m "……"
    
    hide m 2
    show m 3
    
    m "……"

    "聽到有人的呼喚，對方緩緩張開眼睛。"

    hide m 3
    show b black at left

    b "你還好嗎？怎麼倒在這裡！"

    hide b black
    show a wow at right
    
    a "是說…小棠，他該不會是之前寄奇怪信件說要來台南玩請我們帶路的那位吧！"
    
    hide a wow
    show b wow at left
    
    b "！！！"

    b "你這麼一說，他好像跟信件裡附的照片的人長得很像！"
    
    hide b wow
    show b facepalm at left
    show a facepalm at right
    
    "「就算你是外星人，也別用這麼神奇的方式出現吧…」嚴恬與小棠不禁在心中吐槽到。"
    
    hide a facepalm
    hide b facepalm
    show a 1 at right
    show m 3
    
    m "唔…這裡是哪裡啊？"
    
    show b question at left
    
    b "咦？你不記得之前有寫信給我們說要一起遊台南嗎？"
    
    hide m 3
    show m sweat
    
    m "唔…好像有這回事…"

    a "你該不會是失憶了吧？！你還記得怎麼回去你的星球嗎？"

    m "唔…我不記得了…"

    b "那你還記得自己叫什麼名字嗎？"
    
    python:
        povname = renpy.input("【請輸入你的名字】")
        povname = povname.strip();
    
        if not povname:
            povname = "小外星人"
    
    m "[povname]"
    
    hide m sweat
    hide a 1
    show a happy 1 at right
    show b happy at left
    show m happy
    
    a "還好至少你還記得名字，不然就要我們幫你取了呢！"

    b "那我們還是照原本的行程走好了！看能不能一邊幫你恢復記憶，找到回去的方式！"

    b "其實當初我們收到那封信的時候還以為是惡作劇呢！"

    a "對啊，毫無來由的說要我們帶你遊台南，還是個外星人什麼的實在是太可疑了！"
    
    "小棠和嚴恬便覺得不可思議的相視笑道。"
    
    hide a happy 1
    hide b happy
    hide m happy
    
label 台南神學院:

    play music "park_1.wav" fadeout 1.0 fadein 1.0
    
    scene ch 1
    
    window hide
    pause
    
    scene bg 1-1
    window show
    
    show a happy 2 at right
    
    a "巴克禮以前的家就在這裡喔，雖然後來拆掉了。"
    
    show m black
    show b black at left
    
    m "居然把別人家拆了……"
    
    b "不過至少還有留一塊地紀念他的家……"
    
    scene bg 1-2
    
    window hide
    pause
    
    show b happy at left
    
    b "這裡是以哥德式風格的教堂建築、尖塔、尖拱窗西方語彙與臺灣在地紅瓦屋頂，戰後改回水泥瓦的景點。"
    
    play sound "yisell_sound_2008082122472788794_88012.mp3"
    
    a "啊啊啊！"
    
    hide a happy 2
    hide b happy
    show a animal at right
    show b excited at left
    
    b "哇！嚴恬你真的每次來這都會被動物襲擊耶！"
    
    a "不知道為什麼我一直那麼受動物歡迎……"
    
    a "而且小棠你怎麼每次都一臉比我興奮的樣子啊…"
    
    show m wow
    
    m "哇！人類居然會有這樣的體質！"
    
    m "好特別！"
    
    a "你們別用一臉看著稀有物種的表情看著我…"
    
    hide a animal
    hide b excited
    hide m wow
    
    scene bg 1
    
    window hide
    pause
    
    show b happy at left
    show a animal at right
    
    b "這裡還有很豐富的自然環境，很愜意呢！"
    
    a "雖說我常常被襲擊，但我跟小棠還是時常一起來這裡，不管是打球運動或是看書聊天都很合適。"
    
    b "之後我們也來這一起玩吧！"
    
    show m happy
    
    m "好哇！"
    
    hide a animal
    hide b happy
    hide m happy
    stop music
    
label 台灣教會公報社:
    
    scene ch 2
    
    window hide
    pause
    
    scene bg 2
    window show
    
    play music "Pickled Pink.mp3"
    
    show b 1 at left
    
    b "這裡是台灣教會公報社。"
    
    scene bg 3
    
    show a happy 2 at right
    
    a "每次來這邊都會覺得門口這一排書造型的裝置藝術十分有意思呢！"
    
    show b 1 at left
    
    b "對啊。"
    
    hide a happy 2
    hide b 1
    
    scene bg 4
    
    window hide
    pause
    
    show a happy 2 at right
    
    a "一樓展示了一些復古印刷機、打字機…等。"
    
    hide a happy 2
    
    scene bg 6
    window show
    
    show b excited at left
    
    b "身為文具控的我也超想要有一台復古打字機呢！"
    
    hide b excited
    
    scene bg 7
    
    show a happy 2 at right
    
    a "他們有時候還會有復刻版印刷機體驗呢！"
    
    show b lee at left
    
    b "哇！感覺可以揪團來參加看看呢！"
    
    show m excited
    
    m "那我們之後來參加看看吧！"
    
    hide a happy 2
    hide b lee
    hide m excited
    
    scene bg 8
    
    show a 1 at right
    
    a "對了，我還記得翻新之前，這裡的造型奉獻箱就很有名了呢！"
    
    show b happy at left
    
    b "對對對！我們以前也會來這裡投錢看看！"
    
    a "這個箱子看你的錢幣掉到哪個美德裡，就是你目前最缺少的，投下硬幣就可以獲得所對應的「聖靈果子卡」，領受上帝的祝福呢！"
    
    hide a 1
    hide b happy
    show m happy at right
    
    m "真的很特別呢！難得來一趟，我也來玩看看吧！"
    
    play sound "coin_1.wav"
    
    "說完[povname]便投下硬幣，錢幣掉進了「節制」裡。"
    
    hide m happy
    show m 3 at right
    
    show b lee at left
    
    b "看來[povname]是個不太會節制的人呢，哈哈哈！"
    
    hide b lee
    hide m 3
    show a wow at right
    
    a "咦，樓下剛好有一位牧師的畫展呢！"
    
    hide a wow
    show a happy 2 at right
    show b happy at left
    
    b "機會難得，我們去看看吧！"
    
    hide a happy
    hide b happy
    
    scene bg 9
    
    show a happy 2 at right
    
    stop music
    play music "Lovely Piano Song.mp3" fadeout 1.0 fadein 1.0
    
    a "哇，是個很厲害的牧師呢！畫的圖都十分有意境！"
    
    hide a happy 2
    
    scene bg 10
    
    show b happy at left
    
    b "這裡有他的介紹，是李高明牧師油畫、流動畫畫展呢！"
    
    show a 1 at right
    
    a "「服從與約定，從電影畫師到牧師」"
    
    b "原來在三月底的時候他有開分享會。"
    
    hide a 1
    hide b 1
    show m sad
    show b sad at left
    show a sad at right
    
    m "真可惜我們錯過了…"
    
    hide m sad
    hide a sad
    hide b sad
    show a happy 1 at right
    show b happy at left
    show m happy
    
    a "那我們去下一個景點吧！"
    
    hide a happy 1
    hide b happy
    hide m happy
    
label 扭蛋將軍:
    
    stop music
    play music "Pickled Pink.mp3" fadeout 1.0 fadein 1.0
    
    scene ch 11
    
    window hide
    pause
    
    scene bg 11
    window show
    
    show a happy 2 at right
    
    a "這裡是扭蛋將…"
    
    stop music
    
    hide a happy 2
    show a lee at right
    
    play music "Abstract Anxiety.mp3" fadeout 1.0 fadein 1.0
    
    a "咦咦咦咦…等等！小棠怎麼不見了！"
    
    "要陪嚴恬一起找小棠嗎？"
    
    hide a lee
    
menu:

    "一起找":
        jump game
        
    "不找":
        jump end1
        
label game:
    
    show a happy 1 at right
    
    a "那我們就從附近開始找吧！"
    
    show m happy at left
    
    m "那就先在這家店找找看好了。"
    
    hide m happy
    hide a happy 1
    show a wow at right
    
    stop music
    play sound "sound28.mp3"
    
    a "等等…那個不就是小棠嗎！"
    
    jump continue1
    
label end1:
    
    stop music
    play music "Brothers Unite.mp3" fadeout 1.0 fadein 1.0
    
    show black
    with fade
    
    "沒有了小棠的旅途就像是失去了指引的方向，因為嚴恬是路癡一直迷路也沒幫[povname]找到回家的方法，最後[povname]變得無家可歸，漂泊在台南…"
    
    "END"
    
    return
    
label continue1:
    
    play music "Pickled Pink.mp3" fadeout 1.0 fadein 1.0
    
    hide a wow
    
    "眼前一位熟悉的身影正在扭著扭蛋，手上還捧著許多像是剛剛扭到的新玩具們。"
    
    show b ball at left
    
    play sound "whistling.wav"
    
    b "嗯哼哼哼哼～啦啦啦～"
    
    show a angry at right
    
    play music "Nightmare.mp3" fadeout 1.0 fadein 1.0
    
    a "小棠！！！你怎麼又都不說一聲就自己跑去玩！！！"
    
    hide b ball
    show b wow at left
    
    b "！！！"

    b "咦咦咦！怎麼了嗎？"
    
    a "你還問怎麼了！！我們剛剛才話說到一半，你怎麼就突然不見了！！"
    
    hide b wow
    show b sweat at left
    
    b "啊～抱歉抱歉，我突然看到喜歡的動畫出新扭蛋～忍不住就去扭了嘛～"
    
    hide b sweat
    hide a angry
    show m angry
    
    m "害我們白擔心一場了…"
    
    stop music
    play music "Pickled Pink.mp3" fadeout 1.0 fadein 1.0
    
    hide m angry
    show b ball at left
    
    b "欸嘿嘿嘿…"
    
    show a 1 at right
    
    a "唉…總之能找到小棠就好了。"
    
    "嚴恬搖了搖頭說道。"
    
    hide m angry
    hide a 1
    hide b ball
    show b excited at left
    
    b "啊…這裡是扭蛋將軍，是我很喜歡的店喔！時常會進貨一些新的扭蛋跟一番賞喔！"
    
    b "因為我跟嚴恬之前去台北玩的時候發現台北很多這種可以抽一番賞和扭蛋的店家，但台南卻很少這類型的店，所以意外發現這家店的時候，就決定要介紹這裡了！"
    
    hide b excited
    show a happy 2 at right
    
    a "[povname]要不要也玩看看呢？"
    
    hide a happy 2
    
menu:

    "玩！":
        jump play
        
    "不玩。":
        jump noplay
        
label play:

    show m excited
    
    m "玩啊！哪次不玩了！"
    
    m "…那要扭哪個好呢？"
    
    show b excited at left
    
    b "[povname]、嚴恬！！！你們看看這個！！！"
    
    hide m happy
    show m question
    show a question at right
    
    a "怎麼了？"
    
    b "你們看這個扭蛋超可愛的！"
    
    hide m question
    hide a question
    show a happy 1 at right
    show m excited
    
    a "真的欸！"
    
    hide b excited
    show b sad at left
    
    b "嗚嗚嗚…我剛剛花太多在別的上了沒錢抽了…"
    
    hide a happy 1
    show a angry at right
    
    a "齁你真的是…"
    
    hide b sad
    hide a angry
    hide m excited
    show m happy
    
    m "那我扭這個吧！"
    
    show a happy 2 at right
    
    a "好啊。"
    
    hide a happy 2
    show a 1 at right
    show b 1 at left
    
    a "……"
    
    hide a 1
    hide b 1
    show a lee at right
    show b wow at left
    
    a "……等等！！[povname]你怎麼會有台灣的錢！"
    
    hide b wow
    show b black at left
    
    b "該不會你其實…！！"
    
    hide a lee
    hide b black
    hide m happy
    show m facepalm
    
    m "啊啊啊…你們是在想什麼啦！！"
    
    m "我會有你們的錢是因為，我在我的掉下來的地方的地上不知道為什麼凸了一塊。"
    
    m "總覺得下面好像埋了些什麼，所以我就挖看看了。"
    
    m "結果發現裡面放了很多像是紙幣的東西，我就猜這應該是你們台灣交易用的錢幣吧！"
    
    m "總之我想說就拿來當我的旅費吧！"
    
    show a facepalm at right
    show b facepalm at left
    
    a "…希望不是誰不小心掉在那裡的就好…。"
   
    hide m facepalm
    hide a facepalm
    hide b facepalm
    show m happy
   
    m "總之，我來扭看看吧！"
    
    play sound "dropping-2.wav"
    
    "「噠噠噠噠––咚」一顆扭蛋掉出來了。"    
    
    hide m happy
    show b excited at left
    show a wow at right
    
    show m excited
    hide m excited
    show l 2
    
    b "哇！這個是吉祥物的吊飾！"
    
    hide l 2
    show m excited
    
    m "好可愛喔！！"
    
    b "總覺得會很想蒐集一整套呢！"
    
    hide m excited
    hide b excited
    hide a wow
    
    jump continue2
    
label noplay:


    jump continue2
    
label continue2:
    
    play sound "462087__mar-u02144__hungry-stomach.wav"
    
    "咕～～～咕嚕嚕嚕～～～"
    
    show a shy at right
    show b wow at left
    
    b "咦咦，嚴恬原來你餓了嗎？！"
    
    b "那我們要不要先去吃個點心呢？"
    
menu:

    "吃點心！":
        jump eat
        
    "不吃。":
        jump noeat
        
label eat:

    b "嗯…那我們去吃那個吧！"
    
    hide a shy
    show a slaver at right
    
    a "那家嗎！"
    
    show m question
    
    m "？？？"
    
    show b happy at left
    
    b "唉呦走就對了！"
    
    stop music
    play sound "footsteps-4.wav"
    
    hide a slaver
    hide m question
    hide b happy
    
label 桑原商店:
    
    play music "Pickled Pink.mp3" fadeout 1.0 fadein 1.0
    
    scene ch 11-1
    
    window hide
    pause
    
    scene bg 11-1
    with dissolve
    window show
    
    show a slaver at right
    
    a "這熟悉的味道…"
    
    show b slaver at left
    
    b "是桑原商店！！"
    
    a "這邊是仿日式的一間小店，有賣一些甜點，還可以順便在這邊拍照。"
    
    show m wow
    
    m "真的很漂亮呢！"
    
    b "我和嚴恬很喜歡來這邊買點心呢！"
    
    hide m wow
    show l 1
    hide a slaver
    show a happy 2 at right
    
    b "還有賣冰淇淋喔！"
    
    hide l 1
    show m slaver
    
    m "哇！感覺不錯欸！我也要吃看看！"
    
    m "嗯～真好吃欸！"
    
    b "對吧對吧！"
    
    a "那我們吃飽了來去下個景點吧！"
    
    hide m slaver
    hide a happy 2
    hide b slaver
    
    jump continue3
    
label noeat:

    b "好吧！那我們就去下個地點吧！"
    
    hide b happy
    hide a sad
    
    jump continue3
    
label continue3:

label 藝豐漫畫便利屋:    
    scene ch 12
    
    window hide
    pause
    
    scene bg 12
    window show
    
    show a happy 1 at right
    
    a "這裡又是一個小棠很愛來的地方了。"
    
    show b excited at left
    
    b "這裡是藝豐漫畫便利屋！"
    
    b "如果有喜歡的漫畫或是動漫周邊這邊幾乎都買的到喔！"
    
    a "因為常常陪小棠來，發現這裡東西的刷新率很高呢，常常剛出的東西他們就已經上架了。"
    
    b "他們店小小的但東西卻很多，如果有找不到的東西都可以請店員幫忙找喔。"
    
    b "就算店內沒有的東西也可以問看看，請店員幫你訂貨，他們都很親切的喔。"
    
    show m wow
    
    m "真的很不錯呢！"
    
    play sound "footsteps-2.wav"
    
    b "那我們30分鍾店門口見，我去逛了～"
    
    hide b excited
    hide a happy 1
    hide m wow
    show a facepalm at right
    show m facepalm at left
    
    a "跑得真快……"
    
    m "真的……。"
    
    hide a facepalm
    hide m facepalm
    
    "30分鐘後…。"
    
    show a wow at right
    show b excited at left
    
    b "哇喔喔！[povname]你意外的買了很多的漫畫呢！"
    
    b "是不是也體會到了這家店超好買的！"
    
    show m 2
    
    m "是不錯啦…"
    
    hide a wow
    show a happy 1 at right
    
    a "既然逛完了，我們就去下個景點吧！"
    
label 知事官邸生活館:
  
    scene ch 13
    
    window hide
    pause
    
    scene bg 13
    window show
    
    show a happy 1 at right
    
    a "這裡是知事官邸生活館。"
    
    show b happy at left
    
    b "知事官邸生活館是日治時期就建成的，後來也被列為臺南市市定古蹟。"
    
    show m wow
    
    m "嗯～總覺得它跟我印象中的台南古蹟有很大的不同呢！！"
    
    b "對吧對吧！我也覺得這邊超漂亮又很文青！"
    
    a "啊，先別在門口聊了，我們進去看看吧。"
    
    stop music
    play music  "Lucky Break.mp3" fadeout 1.0 fadein 1.0
    
    hide a happy 1
    hide b happy
    hide m wow
    
    scene bg 14
    
    window hide
    pause
    
    scene bg 14
    window show
    
    show b happy at left
    
    b "一進門就會看到天花板上書本造型的裝置藝術。"
    
    show m excited
    
    m "！！！"
    
    m "好特別的裝飾方式！我在以前的星球完全沒看過！"
    
    hide m excited
    
    show a happy 2 at right
    
    a "一樓旁邊有販賣一些文創的小商品，像是杯墊、吊飾…等。"
    
    hide a happy 2
    hide b happy
    
    scene bg 15
    
    window hide
    pause
    
    scene bg 15
    window show
    
    show b 1 at left

    b "二樓一上來，就會看到這邊有一區是販售文創品牌的東西。"
    
    hide b 1
    show m wow at left

    m "哇，都蠻精緻的呢！"
    
    hide m wow
    show m question
    
    m "啊，右邊有一個門欸，是可以出去的嗎？"
    
    show a happy 2 at right 
    
    a "可以啊！"
    
    hide m question
    
    play sound "door-open-7.wav"
    play music  "A Very Brady Special.mp3" fadeout 1.0 fadein 1.0
    
    hide b 1
    hide a happy 2
    
    scene bg 16
    
    window hide
    pause
    
    scene bg 16
    window show
    
    show m happy
    
    m "哇啊，真的好漂亮啊。"
    
    show b happy at left
    
    b "對啊，從這邊可以往下看樓下的花園呢。"
    
    m "這邊的走廊感覺也很適合拍照呢！"
    
    show a happy 1 at right
    
    a "對啊。"
    
    b "那我們也來拍一張吧！"
    
    play sound "camera-click-1.wav"
    
    "喀擦——"
    
    m "這樣就算我回去也還是能常常看照片回味了！"
    
    hide m happy
    hide b happy
    hide a happy
    
    scene bg 17
    
    window hide
    pause
    
    scene bg 17
    window show
    
    stop music
    play music  "Lucky Break.mp3" fadeout 1.0 fadein 1.0
    
    show m wow
    
    m "哇，這邊展示了許多的畫呢！"
    
    show a happy 2 at right
    
    a "對啊，現在展的是「聞歌始覺有人來」，是由十藝家們的創作作品喔！"
    
    show b happy at left
    
    b "這次共展覽了47幅作品呢！"
    
    hide m happy
    hide b happy
    hide a happy
    
    scene bg 18
    
    window hide
    pause
    
    scene bg 18
    window show
    
    show m wow
    
    m "哇，這邊還有展示長餐桌！"
    
    hide m wow
    
    show b wow at left
    
    b "咦你居然知道這個嗎！？"
    
    hide b wow
    show b happy at left
    show a happy 2 at right
    
    a "這種餐桌我和小棠以前都沒看過實體呢！"
    
    hide b happy
    show b sad at left
    
    b "畢竟是很高級昂貴的東西呢。"
    
    hide a happy
    hide b sad
    
    scene bg 19
    
    window hide
    pause
    
    scene bg 19
    window show
    
    show b excited at left
    
    b "哇，假如我是歐洲貴族的書房可能就是長這樣吧！"
    
    hide b excited
    show m 2
    
    m "你還是醒醒吧…"
    
    show a happy 1 at right
    show b happy at left
    
    a "知事官邸生活館真的是個很適合放鬆看展覽的地方呢。"
    
    a "每隔一段時間就會有新的展覽展出喔，可以常常過來看看！"
    
    b "逛了這麼久也說了很多話，有點渴了呢……"
    
    a "那我們帶他一起去台南獨有的飲料店吧！"
    
    hide b happy
    show b excited at left
    
    b "！！！"
    
    b "走吧走吧！"
    
    hide b excited
    hide a happy 1
    hide m 2
    
label 波哥茶飲:
    
    stop music
    play music  "Night in Venice.mp3" fadeout 1.0 fadein 1.0
    
    scene ch 23
    
    window hide
    pause
    
    scene bg 23
    window show
    
    show m slaver
    
    m "哇！一靠近就感覺能聞到茶香呢！"
    
    show b slaver at left
    
    b "嘿嘿嘿～"
    
    hide m slaver
    show m facepalm
    
    m "你幹嘛一臉也很想喝的樣子…"
    
    show a happy 2 at right
    hide m facepalm
    
    a "哈哈，小棠可是道地的台南人呢，也特別喜歡喝手搖！"
    
    hide b slaver
    show b excited at left
    
    b "這間飲料店那麼好喝當然要喝爆了！"    
    
    a "這間飲料店很特別喔，是台南獨有的飲料店！"
    
    b "而且他是在十幾年前飲料店還沒那麼盛行的時候就有的店喔！"
    
    show m excited
    
    m "哇！那真的蠻早的！"
    
    m "我們去點餐吧！"
    
    scene bg 24
    
    window hide
    pause
    
    scene bg 24
    window show
    
    hide b excited 
    show b slaver at left
    
    b "他們的飲料都很不錯喔，很多都是他們特製的！"
    
    hide m excited
    show m slaver
    
    m "哇，那你們有什麼推薦的嗎！"
    
    show a happy 1 at right
    
    a "小棠最愛的就是「綜合新味」莫屬了吧！"
    
    b "當然當然了！"
    
    hide a happy 1
    show a slaver at right
    
    a "我的話蠻喜歡喝他們的玄米茶，很好喝喔！"
    
    hide m slaver
    show m question
    
    m "那我要喝什麼好呢？"
    
    hide b slaver
    show b lee at left
    
    b "啊！他們有一種飲料叫「小幽浮」感覺很適合你喝呢！」"
    
    scene bg 25
    
    window hide
    pause
    
    scene bg 25
    window show
    
    hide m question
    show m slaver
    
    m "那我就喝那個吧！"
    
    scene bg 24
    
    window hide
    pause
    
    scene bg 24
    window show
    
    show a question at right
    
    a "不過話說回來，你有想到你的飛船掉到哪了嗎？"
    
    hide m slaver
    hide b lee
    hide a slaver
    
menu:

    "想到了！":
        jump remember
        
    "還沒想到。":
        jump noremember
        
label remember:
    
    show b excited at left
    
    play sound "sound28.mp3"
    
    b "真的嗎！"
    
    show m excited
    
    m "對啊！"
    
    m "應該也是在這附近！"
    
    b "太好了！！"
    
    show a question at right
    
    a "那你想回去嗎？"
menu:

    "想到要回去還是有點寂寞呢……":
        jump end2
        
    "當然！我想回去自己的星球！":
        jump end3
        
label end2:
    
    hide a question
    hide b excited
    hide m excited
    show b lee at left
    
    b "那你要不要就繼續住在台南呢！"
    
    show m happy
    
    m "嗯…好像可以！"
    
    m "我蠻喜歡台南的！我就住下來吧！"
    
    hide b lee
    show b excited at left
    
    b "太好了！這樣之後我們都還是可以一起玩了！"
    
    show a slaver at right
    
    a "太好了呢！以後還請多多指教了！"
    
    hide a slaver
    hide b excited
    hide m happy
    
    "END"
    
    return
    
label end3:
    
    hide a question
    hide b excited
    hide m excited
    show m 1
    
    m "我果然還是想回去自己的星球呢…"
    
    m "跟你們一起遊台南的這段時間真的很開心！"
    
    m "有機會我還是會再來找你們玩的！"
    
    show b sad at left
    
    b "好吧，再見啦！"
    
    show a sad at right
    
    a "後會有期！"
    
    "END"
    
    return
    
label noremember:    
    
    
    
    jump continue4
    
label continue4:
    
    hide a question
    hide b excited
    hide m excited
    show b lee at left
    
    b "那你先待在台南吧，我們會繼續陪你找你的飛船的！"
    
    show m wow
    
    m "真的可以嗎！"
    
    show a happy 1 at right
    
    a "沒問題的。"
    
    hide a happy 1
    hide b lee
    hide m wow
    
    "在這之後他們也陪了[povname]在台南待了一段時間，終於找到他的飛船了，真是可喜可賀可喜可賀！"
    
    "END"
    
    return