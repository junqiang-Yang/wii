from random import shuffle
Card = ('R','B','2','A','K','Q','J','T','9','8','7','6','5','4','3')#R=大王，B=小王，T=10
#定义玩家
class player:
    name = ''
    lastout = ''
    card = ''
    role = None
    point = 0
    def callord(self,point):
        self.point = point
    def leftcard(self,outcard):
        for i in range(0,len(outcard)):
            self.card = self.card.replace(outcard[i],'',1)
    def initial(self):
        name = ''
        lastout = ''
        self.card = ''
        self.role = None
        self.point = 0
# player1 = player()
# player1.card = '233456789'
# player1.leftcard('345')
# print(player1.card)
#初始化整幅牌
def initialCard():
    stringC = {}
    stringC[0] = 'R'
    stringC[1] = 'B'
    for i in range (0,13):
        stringC[4*i+2]=stringC[4*i+3]=stringC[4*i+4]=stringC[4*i+5]=Card[i+2]
    return ''.join(stringC.values())
#按顺序排列手牌
def dispbyorder(stringF):
    stringS = list(stringF)
    i = len(stringF)-1
    while i > 0:
        for j in range(0,i):
            if Card.index(stringS[j]) > Card.index(stringS[j+1]):
                temp = stringS[j]
                stringS[j] = stringS[j+1]
                stringS[j+1] = temp
        i = i-1
    return ''.join(stringS)
#按顺序排列打出的牌组
def dispcardbyorder(stringF):
    stringS = list(stringF)
    i = len(stringF) - 1
    while i > 0:
        for j in range(0, i):
            if Card.index(stringS[j]) < Card.index(stringS[j + 1]):
            #if stringF.count(stringS[j]) < stringF.count(stringS[j+1]):
                temp = stringS[j]
                stringS[j] = stringS[j + 1]
                stringS[j + 1] = temp
        i = i - 1
    i = len(stringF) - 1
    while i > 0:
        for j in range(0, i):
            #if Card.index(stringS[j]) < Card.index(stringS[j + 1]):
             if stringF.count(stringS[j]) < stringF.count(stringS[j+1]):
                temp = stringS[j]
                stringS[j] = stringS[j + 1]
                stringS[j + 1] = temp
        i = i - 1
    return ''.join(stringS)
#抢地主
def decidelord(p1,p2,p3):
    for p in (p1,p2,p3):
        print('{} call lord:'.format(p.name))
        p.callord(input())
    maxpoint = max(p1.point,p2.point,p3.point)
    for p in (p1,p2,p3):
        if p.point == maxpoint:
            p.role = '地主'
            print('地主是：{}'.format(p.name))
        else:
            p.role = '农民'
#发牌
def fapai(P1,P2,P3):
    stringC1={}
    stringC2={}
    stringC3={}
    stringC = initialCard()
    listC = list(stringC)
    shuffle(listC)
    stringC = ''.join(listC)
    stringD = stringC[51:54]
    for i in range(0,17):
        stringC1[i] = stringC[3*i]
        stringC2[i] = stringC[3*i+1]
        stringC3[i] = stringC[3*i+2]
    P1.card = ''.join(stringC1.values())
    P2.card = ''.join(stringC2.values())
    P3.card = ''.join(stringC3.values())
    print('p1牌组：'+dispbyorder(P1.card))
    print('p2牌组：'+dispbyorder(P2.card))
    print('p3牌组：'+dispbyorder(P3.card))
    print('抢地主')
    decidelord(P1, P2, P3)
    for p in (P1,P2,P3):
        if p.role == '地主':
            p.card = p.card + stringD
        p.card = dispbyorder(p.card)
#检查牌是否是单牌
def checkdanpai(stringF):
    if len(stringF) == 1:
        return 1
    else:
        return 0
#检查牌是否是单对
def checkdandui(stringF):
    if len(stringF) == 2 and stringF[0] == stringF[1]:
        return 2
    else:
        return 0
#检查牌组是否是顺子
def checkshunzi(stringF):
    if len(stringF) < 5:
        return 0
    indexF = {}
    for i in range(len(stringF)):
        indexF[i] = Card.index(stringF[i])
        if Card.index(stringF[i]) < 3:
            return 0
        if stringF.count(stringF[i]) != 1:
            return 0
    maxi = max(indexF.values())
    mini = min(indexF.values())
    if abs(maxi-mini)==len(stringF)-1:
        return 3
    else:
        return 0
#检查牌组是否是连对
def checkliandui(stringF):
    if len(stringF) < 6:
        return 0
    indexF = {}
    for i in range(len(stringF)):
        indexF[i] = Card.index(stringF[i])
        if Card.index(stringF[i]) < 3:
            return 0
        if stringF.count(stringF[i]) != 2:
            return 0
    maxi = max(indexF.values())
    mini = min(indexF.values())
    if abs(maxi-mini) == len(stringF)/2 -1:
        return 4
    else:
        return 0
#检查牌组是否是飞机不带
def checkfeiji(stringF):
    if len(stringF)%3 != 0:
        return 0
    if len(stringF) > 3 and stringF.count('2')==3:
        return 0
    if stringF == '222':
        return 1
    indexF = {}
    for i in range(len(stringF)):
        indexF[i] = Card.index(stringF[i])
        if stringF.count(stringF[i]) != 3:
            return 0
    maxi = max(indexF.values())
    mini = min(indexF.values())
    if abs(maxi-mini) == len(stringF)/3 -1:
        return 5
    else:
        return 0
#检查牌组是否是飞机带单
def checkfeijiD(stringF):
    indexF = {}
    if len(stringF)%4 != 0:
        return 0
    if len(stringF) > 4 and stringF.count('2') == 3:
        return 0
    stringF = dispcardbyorder(stringF)
    for i in range(int(len(stringF)/4*3)):
        if stringF.count(stringF[i]) != 3:
            return 0
    for i in range(int(len(stringF)/4)):
        indexF[i] = Card.index(stringF[3*i])
    maxi = max(indexF.values())
    mini = min(indexF.values())
    if abs(maxi-mini) == int(len(stringF)/4)-1:
        return 6
    else:
        return 0
#检查牌组是否是飞机带双
def checkfeijiS(stringF):
    indexF = {}
    if len(stringF)%5 != 0:
        return 0
    if len(stringF) > 5 and stringF.count('2') == 3:
        return 0
    stringF = dispcardbyorder(stringF)
    for i in range(int(len(stringF)/5*3)):
        if stringF.count(stringF[i]) != 3:
            return 0
    for i in range(int(len(stringF)/5*3),len(stringF)):
        if stringF.count(stringF[i])!=2:
            return 0
    for i in range(int(len(stringF) / 5)):
        indexF[i] = Card.index(stringF[3 * i])
    maxi = max(indexF.values())
    mini = min(indexF.values())
    if abs(maxi - mini) == int(len(stringF) / 5) - 1:
        return 7
    else:
        return 0
#检查牌组是否是四带两张单
def checksidaier(stringF):
    if len(stringF) != 6:
        return 0
    stringF = dispcardbyorder(stringF)
    if stringF.count(stringF[0]) == 4:
        return 8
    else:
        return 0
#检查牌组是否是四带两对
def checksidaidui(stringF):
    if len(stringF) != 8:
        return 0
    stringF = dispcardbyorder(stringF)
    if stringF.count(stringF[0]) != 4:
        return 0
    for i in range(4,len(stringF)):
        if stringF.count(stringF[i]) !=2:
            return 0
    return 9
#检查牌是否是炸弹
def checkzhadan(stringF):
    if len(stringF) == 4 and stringF.count(stringF[0]) == 4:
        return 10
    else:
        return 0
#检查牌是否是王炸
def checkwangzha(stringF):
    if stringF == 'RB' or stringF == 'BR':
        return 11
    else:
        return 0
#比较单牌大小
def comparedanpai(stringF,stringS):
    if Card.index(stringF) > Card.index(stringS):
        return 1
    else:
        return 0
#比较单对大小
def comparedandui(stringF,stringS):
    if Card.index(stringF[0]) > Card.index(stringS[0]):
        return 1
    else:
        return 0
#比较顺子大小
def compareshunzi(stringF,stringS):
    indexF = {}
    indexS = {}
    stringF = dispcardbyorder(stringF)
    stringS = dispcardbyorder(stringS)
    for i in range(len(stringF)):
        indexF[i] = Card.index(stringF[i])
        indexS[i] = Card.index(stringS[i])
    maxF = max(indexF.values())
    maxS = max(indexS.values())
    if maxS < maxF:
        return 1
    else:
        return 0
#比较连对大小
def compareliandui(stringF,stringS):
    indexF = {}
    indexS = {}
    stringF = dispcardbyorder(stringF)
    stringS = dispcardbyorder(stringS)
    for i in range(int(len(stringF)/2)):
        indexF[i] = Card.index(stringF[2*i])
        indexS[i] = Card.index(stringS[2*i])
    maxF = max(indexF.values())
    maxS = max(indexS.values())
    if maxS < maxF:
        return 1
    else:
        return 0
#比较飞机不带大小
def comparefeiji(stringF,stringS):
    stringF = dispcardbyorder(stringF)
    stringS = dispcardbyorder(stringS)
    indexF = {}
    indexS = {}
    for i in range(int(len(stringF) / 3)):
        indexF[i] = Card.index(stringF[3 * i])
        indexS[i] = Card.index(stringS[3 * i])
    maxF = max(indexF.values())
    maxS = max(indexS.values())
    if maxS < maxF:
        return 1
    else:
        return 0
#print(comparefeiji('333','AAA'))
#比较飞机带单的大小
def comparefeijiD(stringF,stringS):
    stringF = dispcardbyorder(stringF)
    stringS = dispcardbyorder(stringS)
    indexF = {}
    indexS = {}
    for i in range(int(len(stringF)/4)):
        indexF[i] = Card.index(stringF[3*i])
        indexS[i] = Card.index(stringS[3*i])
    maxF = max(indexF.values())
    maxS = max(indexS.values())
    if maxS < maxF:
        return 1
    else:
        return 0
#print(comparefeijiS('4443','5554'))
#比较飞机带双的大小
def comparefeijiS(stringF,stringS):
    stringF = dispcardbyorder(stringF)
    stringS = dispcardbyorder(stringS)
    indexF = {}
    indexS = {}
    for i in range(int(len(stringF)/5)):
        indexF[i] = Card.index(stringF[3*i])
        indexS[i] = Card.index(stringS[3*i])
    maxF = max(indexF.values())
    maxS = max(indexS.values())
    if maxS < maxF:
        return 1
    else:
        return 0
#print(comparefeijiS('66633','55544'))
#比较四带二的大小
def comparesidaier(stringF,stringS):
    stringF = dispcardbyorder(stringF)
    stringS = dispcardbyorder(stringS)
    indexS = Card.index(stringS[0])
    indexF = Card.index(stringF[0])
    if indexS < indexF:
        return 1
    else:
        return 0
#print(comparesidaier('333324','555567'))
#比较四带两对的大小
def comparesidaidui(stringF,stringS):
    stringF = dispcardbyorder(stringF)
    stringS = dispcardbyorder(stringS)
    indexS = Card.index(stringS[0])
    indexF = Card.index(stringF[0])
    if indexS < indexF:
        return 1
    else:
        return 0
#比较炸弹的大小
def comparezhadan(stringF,stringS):
    indexF = Card.index(stringF[0])
    indexS = Card.index(stringS[0])
    if indexF > indexS:
        return 1
    else:
        return 0
#print(comparesidaier('33222255','88886677'))
#检查出牌是否符合基本规则以及牌型
def checkBaseRule(stringF):
    #单牌的情况
    if checkdanpai(stringF) != 0:
        #print('单牌')
        return checkdanpai(stringF)
    #单对的情况
    if checkdandui(stringF) != 0:
        #print('单对')
        return checkdandui(stringF)
    #顺子的情况
    if checkshunzi(stringF) != 0:
        #print('顺子')
        return checkshunzi(stringF)
    #连对的情况
    if checkliandui(stringF) != 0:
        #print('连对')
        return checkliandui(stringF)
    #飞机不带的情况
    if checkfeiji(stringF) != 0:
        #print('飞机不带')
        return checkfeiji(stringF)
    #飞机带单的情况
    if checkfeijiD(stringF) != 0:
        #print('飞机带单')
        return checkfeijiD(stringF)
    #飞机带双的情况
    if checkfeijiS(stringF) != 0:
        #print('飞机带双')
        return checkfeijiS(stringF)
    #四带两张单的情况
    if checksidaier(stringF) != 0:
        #print('四带二')
        return checksidaier(stringF)
    #四带两对的情况
    if checksidaidui(stringF) != 0:
        #print('四带两对')
        return checksidaidui(stringF)
    #炸弹的情况
    if checkzhadan(stringF) != 0:
        #print('炸弹')
        return checkzhadan(stringF)
    #王炸的情况
    if checkwangzha(stringF) != 0:
        #print('王炸')
        return checkwangzha(stringF)
    print('牌组不符合规则')
    return 0
#print(checkBaseRule('AAAKKK2233'))
#比较所选牌组是否大过上家
def comparepaizu(stringF,stringS):
    if checkwangzha(stringS) > 0:
        return 1
    if checkwangzha(stringF) > 0:
        return 0
    if checkzhadan(stringF) > 0 and checkzhadan(stringS) == 0:
        return 0
    if checkzhadan(stringS) > 0 and checkzhadan(stringF) == 0 :
        return 1
    ftype = checkBaseRule(stringF)
    stype = checkBaseRule(stringS)
    if len(stringF) != len(stringS):
        return 0
    if ftype != stype:
        return 0
    if ftype == 1:
        return comparedanpai(stringF,stringS)
    elif ftype == 2:
        return comparedandui(stringF,stringS)
    elif ftype == 3:
        return compareshunzi(stringF,stringS)
    elif ftype == 4:
        return compareliandui(stringF,stringS)
    elif ftype == 5:
        return comparefeiji(stringF,stringS)
    elif ftype == 6:
        return comparefeijiD(stringF,stringS)
    elif ftype == 7:
        return comparefeijiS(stringF,stringS)
    elif ftype == 8:
        return comparesidaier(stringF,stringS)
    elif ftype == 9:
        return comparesidaidui(stringF,stringS)
def iswinner(p):
    if p.card == '':
        print('{}赢了'.format(p.role))
        return 1
    else:
        return 0
def round(p1,p2,p3,flag1,flag2,outcard1):
    maxcard = ''
    if flag1 == 1:
        print('{}出牌'.format(p1.name))
        outcard1 = input()
        while True:
            if checkBaseRule(outcard1) == 0 or outcard1 == '':
                print('出牌不符合规则,重新输入：')
                outcard1 = input()
            elif checkBaseRule(outcard1) > 0:
                maxcard = outcard1
                p1.lastout = outcard1
                p1.leftcard(outcard1)
                break
        print('{}打出：{}'.format(p1.name,dispcardbyorder(outcard1)))
        if iswinner(p1) > 0:
            print('游戏结束')
            return 0
    elif flag1 == 0:
        maxcard = outcard1
    if flag2 == 1:
        print('{}出牌'.format(p2.name))
        outcard2 = input()
        while True:
            if outcard2 == 'p':
                p2.lastout = ''
                break
            elif checkBaseRule(outcard2) ==0 or comparepaizu(maxcard,outcard2) == 0:
                print('出牌不符合规则，重新输入：')
                outcard2 = input()
            elif comparepaizu(maxcard,outcard2) > 0:
                maxcard = outcard2
                p2.lastout = outcard2
                p2.leftcard(outcard2)
                break
        if outcard2 == 'p':
            print('{}pass'.format(p2.name))
        else:
            print('{}打出：{}'.format(p2.name, dispcardbyorder(outcard2)))
        if iswinner(p2) > 0:
            print('游戏结束')
            return 0
    print('{}出牌'.format(p3.name))
    outcard3 = input()
    while True:
        if outcard3 == 'p':
            p3.lastout = ''
            break
        elif checkBaseRule(outcard3) == 0 or comparepaizu(maxcard,outcard3) == 0:
            print('出牌不符合规则，重新输入：')
            outcard3 = input()
        elif comparepaizu(maxcard, outcard3) > 0:
            maxcard = outcard3
            p3.lastout = outcard3
            p3.leftcard(outcard3)
            break
    if outcard3 == 'p':
        print('{}pass'.format(p3.name))
    else:
        print('{}打出：{}'.format(p3.name, dispcardbyorder(outcard3)))
    if iswinner(p3) > 0:
        print('游戏结束')
        return 0
    print('各玩家所剩牌组:')
    print('{}牌组：{}'.format(p1.name,dispbyorder(p1.card)))
    print('{}牌组：{}'.format(p2.name,dispbyorder(p2.card)))
    print('{}牌组：{}'.format(p3.name,dispbyorder(p3.card)))
    if p1.lastout == maxcard:
        round(p1,p2,p3,1,1,'')
    elif p2.lastout == maxcard:
        round(p2,p3,p1,0,0,maxcard)
    elif p3.lastout == maxcard:
        round(p3,p1,p2,0,1,maxcard)
def newgame():
    print('游戏开始')
    player1 = player()
    player2 = player()
    player3 = player()
    player1.name = 'p1'
    player2.name = 'p2'
    player3.name = 'p3'
    print('发牌')
    fapai(player1,player2,player3)
    print('{}牌组:{}'.format(player1.name,player1.card))
    print('{}牌组:{}'.format(player2.name,player2.card))
    print('{}牌组:{}'.format(player3.name,player3.card))
    if player1.role == '地主':
        round(player1,player2,player3,1,1,'')
    elif player2.role == '地主':
        round(player2, player3, player1,1,1,'')
    elif player3.role == '地主':
        round(player3, player1, player2,1,1,'')
newgame()