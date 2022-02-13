import cv2
import numpy as np
import time

movee = 0
game = 0
check = 0

ten = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

cam = cv2.VideoCapture(1)

def main1():
    img1 = cv2.imread("opencvframe0.png", 0)
    ref = cv2.imread("refrenece.png", 0)
    img = cv2.resize(img1, (600, 600))
    # ten = 0
    global movee
    global ten
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

    crop_img11 = img[135:200, 400:460]  # 11
    crop_img12 = img[260:325, 400:440]  # 12
    crop_img13 = img[390:460, 400:430]  # 13
    crop_img21 = img[130:200, 320:370]  # 21
    crop_img22 = img[260:330, 320:365]  # 22
    crop_img23 = img[380:455, 317:360]  # 23
    crop_img31 = img[125:195, 230:265]  # 31
    crop_img32 = img[250:320, 220:260]  # 32
    crop_img33 = img[380:455, 220:260]  # 33

    error = 0

    resizeref = cv2.resize(ref, (50, 50))
    resize11 = cv2.resize(crop_img11, (50, 50))
    resize33 = cv2.resize(crop_img33, (50, 50))
    resize22 = cv2.resize(crop_img22, (50, 50))
    resize21 = cv2.resize(crop_img21, (50, 50))
    resize12 = cv2.resize(crop_img12, (50, 50))
    resize13 = cv2.resize(crop_img13, (50, 50))
    resize23 = cv2.resize(crop_img23, (50, 50))
    resize31 = cv2.resize(crop_img31, (50, 50))
    resize32 = cv2.resize(crop_img32, (50, 50))

    out1 = np.zeros((50, 50))
    out2 = np.zeros((50, 50))
    out3 = np.zeros((50, 50))
    movee = 0
    while (1):
        error = 0
        if (ten == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize11[x, y]
                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                movee = 1
                ten = 1
                break
        error = 0
        if (two == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize12[x, y]

                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                movee = 2
                two = 1
                break
        error = 0
        if (three == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize13[x, y]
                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                movee = 3
                three = 1
                break
        error = 0
        if (four == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize21[x, y]
                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                movee = 4
                four = 1
                break
        error = 0
        if (five == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize22[x, y]
                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                movee = 5
                five = 1
                break
        error = 0
        if (six == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize23[x, y]
                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                six = 1
                movee = 6
                break
        error = 0
        if (seven == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize31[x, y]
                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                movee = 7
                seven = 1
                break
        error = 0
        if (eight == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize32[x, y]

                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                eight = 1
                movee = 8
                break
        error = 0
        if (nine == 0):
            for x in range(0, 50):
                for y in range(0, 50):

                    out1[x, y] = resizeref[x, y] - resize33[x, y]

                    if (out1[x, y] > 80 and out1[x, y] < 200):
                        error += 1
            if (error > 10):
                nine = 1
                movee = 9
                break
        if (movee == 0):
            break


def test(moves):
    print(moves)


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
            bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                   bo[2] == le and bo[5] == le and bo[8] == le) or (
                   bo[3] == le and bo[6] == le and bo[9] == le) or (
                   bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove(move):
    print("User has played", move)

    if move > 0 and move < 10:
        if spaceIsFree(move):

            insertLetter('X', move)
        else:
            print('Sorry, this space is occupied!')
    else:
        print('Please type a number within the range!')


board = [' ' for x in range(10)]


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def mainn(movee):
    global game
    global ten
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine


    if (game == 0):
        if not (isWinner(board, 'O')):
            playerMove(movee)
        # printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            game = 1

    if (game == 0):
        dataa = 100
        if not (isWinner(board, 'X')):
            move = compMove()
            if (move == 1):
                ten = 1
                file2 = open("A.txt", 'w')
                file2.write("1")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 2):
                two = 1
                file2 = open("A.txt", 'w')
                file2.write("2")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 3):
                three = 1
                file2 = open("A.txt", 'w')
                file2.write("3")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 4):
                four = 1
                file2 = open("A.txt", 'w')
                file2.write("4")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 5):
                five = 1
                file2 = open("A.txt", 'w')
                file2.write("5")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 6):
                six = 1
                file2 = open("A.txt", 'w')
                file2.write("6")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 7):
                seven = 1
                file2 = open("A.txt", 'w')
                file2.write("7")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 8):
                eight = 1
                file2 = open("A.txt", 'w')
                file2.write("8")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if (move == 9):
                nine = 1
                file2 = open("A.txt", 'w')
                file2.write("9")
                file2.close()
                time.sleep(1)
                file2 = open("A.txt", 'r')
                dataa = int(file2.read())
                file2.close()
                time.sleep(1)
                while (dataa != 30):
                    file2 = open("A.txt", 'r')
                    dataa = int(file2.read())
                    file2.close()
                    print("waiting")
                    time.sleep(3)
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
            # printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            game = 1

    if (game == 0):
        if isBoardFull(board):
            print('Tie Game!')
            game = 1


while (game == 0):
    print("code running")
    ret, frame = cam.read()
    img_name = "opencvframe{}.png".format(0)
    cv2.imwrite(img_name, frame)
    main1()
    mainn(movee)
    time.sleep(2)
cam.release()

cv2.waitKey(0)
