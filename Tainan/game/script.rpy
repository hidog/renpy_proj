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
label 光華校門口:

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
    
    show b happy at left
    
    b "太好了！"

    a "對了小棠今天要來我們家一起…"
    
    hide a happy 1
    hide b happy
    
    "「咚———」"
    
    show b wow at left
    
    b "……咦咦咦？！"

    b "前面是不是發生什麼事了！" 
    
    hide b wow
    
    "「噠噠噠噠—」聽到奇怪的聲響後，小棠和嚴恬便加快腳步往聲音方向走去。"
    
    show a wow at right
    
    a "有個人倒在那裡！"
    
    hide a wow
    show a 1 at right
    show b 1 at left
    
    "看到有人有困難，小棠和嚴恬便急忙跑去攙扶對方，輕輕搖醒對方。"
    
    hide a 1
    hide b 1
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
    show b wow at left

    b "你還好嗎？怎麼倒在這裡！"

    hide b wow
    show a wow at right
    
    a "是說…小棠，他該不會是之前寄奇怪信件說要來台南玩請我們帶路的那位吧！"
    
    hide a wow
    show b wow at left
    
    b "！！！"

    b "你這麼一說，他好像跟信件裡附的照片的人長得很像！"
    
    hide b wow
    show b 1 at left
    show a 1 at right
    
    "「就算你是外星人，也別用這麼神奇的方式出現吧…」嚴恬與小棠不禁在心中吐槽到。"
    
    show m 3
    
    m "唔…這裡是哪裡啊？"
    
    b "咦？你不記得之前有寫信給我們說要一起遊台南嗎？"
    
    m "唔…好像有這回事…"

    a "你該不會是失憶了吧？！你還記得怎麼回去你的星球嗎？"

    m "唔…我不記得了…"

    b "那你還記得自己叫什麼名字嗎？"
    
    python:
        povname = renpy.input("你的名字是什麼？")
        povname = povname.strip();
    
        if not povname:
            povname = "主人公"
    
    m "[povname]"

    a "還好至少你還記得名字，不然就要我們幫你取了呢！"

    b "那我們還是照原本的行程走好了！看能不能一邊幫你恢復記憶，找到回去的方式！"

    b "其實當初我們收到那封信的時候還以為是惡作劇呢！"

    a "對阿，毫無來由的說要我們帶你遊台南，還是個外星人什麼的實在是太可疑了！"
    
    hide a 1
    hide b 1
    show a happy 1 at right
    show b happy at left
    
    "小棠和嚴恬便覺得不可思議的相視笑道。"
    
    hide a happy 1
    hide b happy
    hide m 3
    
label 台南神學院:

    scene ch 1
    
    window hide
    pause
    
    scene bg 1
    window show
    
    show a happy 2 at right
    
    a "這邊是我跟小棠時常一起活動的地方，我們常常一起在這邊打球運動，或是看書聊天也都在這裡。"
    
    show b happy at left
    
    b "之後我們也來這一起玩吧！"
    
    hide a happy 2
    hide b happy
    
label 台灣教會公報社:
    
    scene ch 2
    
    window hide
    pause
    
    scene bg 2
    window show
    
    "台灣教會公報社"
    
    show b 1 at left

    b "這裡是台灣教會公報社。"

    scene bg 3
    
    show a happy 2 at right
    
    a "每次來這邊都會覺得門口這一排書造型的裝置藝術十分有意思呢！"
    
    show b 1 at left
    
    b "對阿。"
    
    hide a happy 2
    hide b 1
    
    scene bg 4
    
    window hide
    pause
    
    " "
    
    scene bg 5
    
    window hide
    pause
    
    " "
    
    scene bg 6
    window show
    
    show b happy at left
    
    b "一樓展示了一些復古印刷機、打字機…等，身為文具控的我也超想要有一台復古打字機呢！"
    
    hide b happy
    
    scene bg 7
    
    show a happy 2 at right
    
    a "他們有時候還會開復刻版印刷機體驗呢！"
    
    show b happy at left
    
    b "哇！感覺可以揪團來參加看看呢！"
    
    show m happy
    
    m "那我們之後來參加看看吧！"
    
    hide a happy 2
    hide b happy
    hide m happy
    
    scene bg 8
    
    show a 1 at right
    
    a "對了，我還記得翻新之前，這裡的造型奉獻箱就很有名了呢！"
    
    show b 1 at left
    
    b "對對對！我們以前也會來這裡投錢看看！"

    a "這個箱子看你的錢幣掉到哪個美德裡，就是你目前最缺少的，投下硬幣就可以獲得所對應的「聖靈果子卡」，領受上帝的祝福呢！"
    
    hide a 1
    hide b 1
    show m happy at right
    
    m "真的很特別呢！難得來一趟，我也來玩看看吧！"

    "說完[povname]便投下硬幣，錢幣掉進了「節制」裡。"

    hide m happy
    show m 3 at right

    show b happy at left

    b "看來[povname]是個不太會節制的人呢，哈哈哈！"

    hide b happy
    hide m 3
    show a wow at right
    
    a "咦，樓下剛好有一位牧師的畫展呢！"
    
    hide a wow
    show a 1 at right
    show b 1 at left

    b "機會難得，我們去看看吧！"
    
    hide a 1
    hide b 1
    
    scene bg 9
    
    show a happy 2 at right
    
    a "哇，是個很厲害的牧師呢！畫的圖都十分有意境！"
    
    hide a happy 2
    
    scene bg 10
    
    show b 1 at left
    
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
    
    scene ch 11
    
    window hide
    pause
    
    scene bg 11
    window show
    
    show a happy 2 at right
    
    a "這裡是扭蛋將…"
    
    hide a happy 2
    show a wow at right
    
    a "咦咦咦咦…等等！小棠怎麼不見了！"
    
    "要陪嚴恬一起找小棠嗎？"
    
    hide a wow
    
menu:

    "一起找":
        jump game
        
    "不找":
        jump end1
        
label game:
    
    show a happy 1 at right
    
    a "那我們就就近開始找吧！"
    
    show m happy at left
    
    m "那就先在這家店找找看"
    
    hide m happy
    hide a happy 1
    show a wow at right
    
    a "等等…那個不就是小棠嗎！"
    
    jump continue1
    
label end1:
    
    show black
    with fade
    
    "沒有了小棠的旅途就像是失去了指引的方向，因為嚴恬是路癡一直迷路也沒幫[povname]找到回家的方法，最後[povname]變得無家可歸，漂泊在台南…"
    
    "end"
    
    return
    
label continue1:
    
    hide a wow
    
    "眼前一位熟悉的身影正在扭著扭蛋，手上還捧著許多像是剛剛扭到的新玩具們。"
    
    show b happy
    
    b "嗯哼哼哼哼～啦啦啦～"
    
    hide b happy
    show b happy at left
    show a 1 at right
    
    a "小棠！！！你怎麼又都不說一聲就自己跑去玩！！！"
    
    hide b happy
    show b wow at left
    
    b "！！！"

    b "咦咦咦！怎麼了嗎？"
    
    a "你還問怎麼了！！我們剛剛才話說到一半，你怎麼就突然不見了！！"
    
    b "啊～抱歉抱歉，我突然看到喜歡的動畫出新一番賞～忍不住就去抽了嘛～"
    
    hide b wow
    hide a 1
    show m 2
    
    m "害我們白擔心一場了…"
    
    show b 1 at left
    
    b "欸嘿嘿嘿…"
    
    show a 1 at right
    
    a "唉…總之能找到小棠就好了。"
    
    "嚴恬搖了搖頭說道。"
    
    hide m 2
    hide a 1
    hide b 1
    show b happy at left
    
    b "啊…這裡是扭蛋將軍，是我很喜歡的店喔！時常會進貨一些新的扭蛋跟一番賞喔！"
    
    b "因為我跟嚴恬之前去台北玩的時候發現台北很多這種可以抽一番賞和扭蛋的店家，但台南卻很少這類型的店，所以意外發現這家店的時候，就決定要介紹這裡了！"
    
    hide b happy
    show a happy 2 at right
    
    a "[povname]要不要也玩看看呢？"
    
    hide a happy 2
    
menu:

    "玩！":
        jump play
        
    "不玩。":
        jump noplay
        
label play:

    show m happy
    
    m "玩啊！哪次不玩了！"
    
    m "…那要扭哪個好呢？"
    
    show b happy at left
    
    b "[povname]、嚴恬！！！你們看看這個！！！"
    
    hide m happy
    show m wow
    show a wow at right
    
    a "怎麼了？"
    
    b "你們看這個扭蛋超可愛的！"
    
    a "真的欸！"
    
    hide b happy
    show b sad at left
    
    b "嗚嗚嗚…我剛剛花太多在別的上了沒錢抽了…"
    
    a "齁你真的是…"
    
    hide b sad
    hide a wow
    hide m wow
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
    show a wow at right
    show b wow at left
    
    a "……等等！！[povname]你怎麼會有台灣的錢！"
    
    b "該不會你其實…！！"
    
    hide a wow
    hide b wow
    hide m happy
    show m 3
    
    m "啊啊啊…你們是在想什麼啦！！"
    
    m "我會有你們的錢是因為，我在我的掉下來的地方的地上不知道為什麼凸了一塊。"
    
    m "總覺得下面好像埋了些什麼，所以我就挖看看了。"
    
    m "結果發現裡面放了很多像是紙幣的東西，我就猜這應該是你們台灣交易用的錢幣吧！"
    
    m "總之我想說就拿來當我的旅費吧！"
    
    show a 1 at right
    show b 1 at left
    
    a "…希望不是誰不小心掉在那裡的就好…。"
   
    m "總之，我來扭看看吧！"
    
    "「噠噠噠噠––咚」一顆扭蛋掉出來了。"   
    
    hide a 1
    hide b 1
    hide m 3
    show m happy
    show b wow at left
    show a wow at right
    
    b "哇！這個是吉祥物的吊飾！"
    
    m "好可愛喔！！"
    
    b "總覺得會很想蒐集一整套呢！"
    
    hide m happy
    hide b wow
    hide a wow
    
    jump continue2
    
label noplay:


    jump continue2
    
label continue2:

    "咕～～～咕嚕嚕嚕～～～"
    
    show a sad at right
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
    
    hide a sad
    show a happy 1 at right
    
    a "那家嗎！"
    
    show m 2
    
    m "？？？"
    
    show b happy at left
    
    b "唉呦走就對了！"
    
    hide a happy 1
    hide m 2
    hide b happy
    
label 桑原商店:
    
    scene ch 11-1
    
    window hide
    pause
    
    scene bg 11-1
    with dissolve
    window show
    
    show a happy 1 at right
    
    a "這熟悉的味道…"
    
    show b happy at left
    
    b "是桑原商店！！"
    
    a "這邊是仿日式的一間小店，有賣一些甜點，還可以順便在這邊拍照。"
    
    show m wow
    
    m "真的很漂亮呢！"
    
    b "我和嚴恬很喜歡來這邊買點心呢！"
    
    hide m wow
    show l 1
    hide a happy 1
    show a happy 2 at right
    
    b "還有賣冰淇淋喔！"
    
    hide l 1
    show m happy
    
    m "哇！感覺不錯欸！我也要吃看看！"
    
    m "嗯～真好吃欸！"
    
    b "對吧對吧！"
    
    a "那我們吃飽了來去下個景點吧！"
    
    hide m happy
    hide a happy 2
    hide b happy
    
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
    
    show b happy at left
    
    b "這裡是藝豐漫畫便利屋！"
    
    b "如果有喜歡的漫畫或是動漫周邊這邊幾乎都買的到喔！"
    
    a "因為常常陪小棠來，發現這裡東西的刷新率很高呢，常常剛出的東西他們就已經上架了。"
    
    b "他們店小小的但東西卻很多，如果有找不到的東西都可以請店員幫忙找喔。"
    
    b "就算店內沒有的東西也可以問看看，請店員幫你訂貨，他們都很親切的喔。"
    
    show m wow
    
    m "真的很不錯呢！"
    
    b "那我們30分鍾店門口見，我去逛了～"
    
    hide b happy
    hide a happy 1
    hide m wow
    show a 1 at right
    show m 2 at left
    
    a "跑得真快……"
    
    m "真的……。"
    
    hide a 1
    hide m 2
    
    "30分鐘後…。"
    
    show a wow at right
    show b wow at left
    
    b "哇喔喔！[povname]你意外的買了很多的漫畫呢！"
    
    hide b wow
    show b happy
    
    b "是不是也體會到了這家店超好買的！"
    
    show m 2
    
    m "是不錯啦…"
    
    hide a wow
    show a happy 1
    
    a "既然逛完了，我們就去下個景點吧！"
    
label 知事官邸:
  
    scene ch 13
    
    window hide
    pause
    
    scene bg 13
    window show
    
    return