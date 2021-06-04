init:
    $ style.default.font = "msjh.ttc"
    $ style.default.language = "msjh"
init python:
   style.default.layout = "greedy"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("嚴恬")
define b = Character("小棠")
# define m = Character("主人公", color="#c8c8f")
define m = Character("[povname]")

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

    python:
        povname = "???"

    scene bg 0

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

    scene bg 1
    
    show a happy 2 at right
    
    a "這邊是我跟小棠時常一起活動的地方，我們常常一起在這邊打球運動，或是看書聊天也都在這裡。"
    
    show b happy at left
    
    b "之後我們也來這一起玩吧！"
    
    hide a happy 2
    hide b happy
    
label 台灣教會公報社:
    
    scene bg 2
    
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
    
    " "
    
    scene bg 5
    
    " "
    
    scene bg 6
    
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

    return