import sys, os, string, pygame
import pygame.freetype
import numpy as np

pygame.init()
size = width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
pyFont = pygame.freetype.Font(None)

background = pygame.image.load('background.png')
backRect = background.get_rect()
gallows = pygame.image.load('gallows.png')
gallowsRect = gallows.get_rect()
gallowsRect = gallowsRect.move([300, 200])

winScreen = pygame.image.load('winScreen.png')
winRect = winScreen.get_rect()
loseScreen = pygame.image.load('loseScreen.png')
loseRect = loseScreen.get_rect()

#Checks if word to guess is set
wordSet = False
confirm = False
word = []
clueWord = []
wordLen = 0
prompt = pygame.image.load('prompt.png')
promptRect = prompt.get_rect()
promptRect = promptRect.move([50, 50])
basePromptRect = prompt.get_rect()
basePromptRect = basePromptRect.move([50,50])

#Guess and guess prompt
currentGuess = ':'
occurances = 0
incorrectGallery = []
confirmGuess = False
confirmed = False
statUpdate = False
statPrompt = pygame.image.load('statsPrompt.png')
statPromptRect = statPrompt.get_rect()
statPromptRect = statPromptRect.move([10, 10])
guessPrompt = pygame.image.load('promptBase.png')
guessPromptRect = guessPrompt.get_rect()
guessPromptRect = guessPromptRect.move([10, 275])
confirmGuessPrompt = pygame.image.load('promptConfirmGuess.png')
CGPRect = confirmGuessPrompt.get_rect()
CGPRect = CGPRect.move([10, 275])

winCondition = False
loseCondition = False

maxAttemptsLeft = 6
incorrectAttempts = 0
headBasic = pygame.image.load('headBasic.png')
headRect = headBasic.get_rect()
headRect = headRect.move([530, 250])
body = pygame.image.load('body.png')
bodyRect = body.get_rect()
bodyRect = bodyRect.move([560, 340])
leftArm = pygame.image.load('leftArm.png')
leftARect = leftArm.get_rect()
leftARect = leftARect.move([488, 300])
rightArm = pygame.image.load('rightArm.png')
rightARect = rightArm.get_rect()
rightARect = rightARect.move([582,300])
leftLeg = pygame.image.load('leftLeg.png')
leftLRect = leftLeg.get_rect()
leftLRect = leftLRect.move([485, 465])
rightLeg = pygame.image.load('rightLeg.png')
rightLRect = rightLeg.get_rect()
rightLRect = rightLRect.move([585, 465])

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				if(not wordSet):
					word.append('A')
				else:
					currentGuess = 'A'
			elif event.key == pygame.K_b:
				if(not wordSet):
					word.append('B')
				else:
					currentGuess = 'B'
			elif event.key == pygame.K_c:
				if(not wordSet):
					word.append('C')
				else:
					currentGuess = 'C'
			elif event.key == pygame.K_d:
				if(not wordSet):
					word.append('D')
				else:
					currentGuess = 'D'
			elif event.key == pygame.K_e:
				if(not wordSet):
					word.append('E')
				else:
					currentGuess = 'E'
			elif event.key == pygame.K_f:
				if(not wordSet):
					word.append('F')
				else:
					currentGuess = 'F'
			elif event.key == pygame.K_g:
				if(not wordSet):
					word.append('G')
				else:
					currentGuess = 'G'
			elif event.key == pygame.K_h:
				if(not wordSet):
					word.append('H')
				else:
					currentGuess = 'H'
			elif event.key == pygame.K_i:
				if(not wordSet):
					word.append('I')
				else:
					currentGuess = 'I'
			elif event.key == pygame.K_j:
				if(not wordSet):
					word.append('J')
				else:
					currentGuess = 'J'
			elif event.key == pygame.K_k:
				if(not wordSet):
					word.append('K')
				else:
					currentGuess = 'K'
			elif event.key == pygame.K_l:
				if(not wordSet):
					word.append('L')
				else:
					currentGuess = 'L'
			elif event.key == pygame.K_m:
				if(not wordSet):
					word.append('M')
				else:
					currentGuess = 'M'
			elif event.key == pygame.K_n:
				if(not wordSet):
					word.append('N')
				else:
					currentGuess = 'N'
			elif event.key == pygame.K_o:
				if(not wordSet):
					word.append('O')
				else:
					currentGuess = 'O'
			elif event.key == pygame.K_p:
				if(not wordSet):
					word.append('P')
				else:
					currentGuess = 'P'
			elif event.key == pygame.K_q:
				if(not wordSet):
					word.append('Q')
				else:
					currentGuess = 'Q'
			elif event.key == pygame.K_r:
				if(not wordSet):
					word.append('R')
				else:
					currentGuess = 'R'
			elif event.key == pygame.K_s:
				if(not wordSet):
					word.append('S')
				else:
					currentGuess = 'S'
			elif event.key == pygame.K_t:
				if(not wordSet):
					word.append('T')
				else:
					currentGuess = 'T'
			elif event.key == pygame.K_u:
				if(not wordSet):
					word.append('U')
				else:
					currentGuess = 'U'
			elif event.key == pygame.K_v:
				if(not wordSet):
					word.append('V')
				else:
					currentGuess = 'V'
			elif event.key == pygame.K_w:
				if(not wordSet):
					word.append('W')
				else:
					currentGuess = 'W'
			elif event.key == pygame.K_x:
				if(not wordSet):
					word.append('X')
				else:
					currentGuess = 'X'
			elif event.key == pygame.K_y:
				if(not wordSet):
					word.append('Y')
				else:
					currentGuess = 'Y'
			elif event.key == pygame.K_z:
				if(not wordSet):
					word.append('Z')
				else:
					currentGuess = 'Z'
			elif event.key == pygame.K_SPACE:
				if(not wordSet):
					word.append(' ')
			elif event.key == pygame.K_0:
				if(not wordSet):
					word.append('0')
				else:
					currentGuess = '0'
			elif event.key == pygame.K_1:
				if(not wordSet):
					word.append('1')
				else:
					currentGuess = '1'
			elif event.key == pygame.K_2:
				if(not wordSet):
					word.append('2')
				else:
					currentGuess = '2'
			elif event.key == pygame.K_3:
				if(not wordSet):	
					word.append('3')
				else:
					currentGuess = '3'
			elif event.key == pygame.K_4:
				if(not wordSet):
					word.append('4')
				else:
					currentGuess = '4'
			elif event.key == pygame.K_5:
				if(not wordSet):
					word.append('5')
				else:
					currentGuess = '5'
			elif event.key == pygame.K_6:
				if(not wordSet):
					word.append('6')
				else:
					currentGuess = '6'
			elif event.key == pygame.K_7:
				if(not wordSet):
					word.append('7')
				else:
					currentGuess = '7'
			elif event.key == pygame.K_8:
				if(not wordSet):
					word.append('8')
				else:
					currentGuess = '8'
			elif event.key == pygame.K_9:
				if(not wordSet):
					word.append('9')
				else:
					currentGuess = '9'
			elif event.key == pygame.K_COLON:
				if(not wordSet):
					word.append(':')
			elif event.key == pygame.K_SEMICOLON:
				if(not wordSet):	
					word.append(';')
			elif event.key == pygame.K_MINUS:
				if(not wordSet):
					word.append('_')
			elif event.key == pygame.K_ESCAPE:
				if not wordSet:
					prompt = pygame.image.load('prompt.png')
					promptRect = prompt.get_rect()
					promptRect = promptRect.move([50, 50])
					confirm = False
					wordSet = False
				else:
					currentGuess = ':'
					confirmGuess = False
					confirmed = False
					guessPrompt = pygame.image.load('promptBase.png')
					guessPromptRect = guessPrompt.get_rect()
					guessPromptRect = guessPromptRect.move([10, 275])
					wordIndex = 0
					for l in word:
						if l == ';' or l == ':' or l == '_' or l == ' ':
							clueWord[wordIndex] = True
							occurances = occurances + 1
						if clueWord[wordIndex] == True:
							guessPromptRect = pyFont.render_to(guessPrompt, (10+(25 * wordIndex), 25), word[wordIndex], bgcolor=None, style=0,rotation=0, size=24)
						else:
							guessPromptRect = pyFont.render_to(guessPrompt, (10+(25 * wordIndex), 25), '_ ', bgcolor=None, style=0,rotation=0, size=24)
						wordIndex = wordIndex + 1
					guessPromptRect = guessPromptRect.move([10, 275])
					confirmGuessPrompt = pygame.image.load('promptConfirmGuess.png')
					CGPRect = confirmGuessPrompt.get_rect()
					CGPRect = CGPRect.move([10, 275])
			elif event.key == pygame.K_BACKSPACE:
				if len(word) > 0 and not wordSet:
					word.pop()
					prompt = pygame.image.load('prompt.png')
					promptRect = prompt.get_rect()
					promptRect = promptRect.move([50, 50])
			elif event.key == pygame.K_RETURN:
				if not wordSet:
					if(not confirm):
						prompt = pygame.image.load('confirmPrompt.png')
						promptRect = prompt.get_rect()
						promptRect = promptRect.move([50,50])
						confirm = True
					else:
						wordSet = True
				elif((not currentGuess == ':') and confirmGuess == False):
					confirmGuess = True
				elif winCondition or loseCondition:
					winCondition = False
					loseCondition = False
					maxAttemptsLeft = 6
					incorrectAttempts = 0
					currentGuess = ':'
					occurances = 0
					incorrectGallery = []
					confirmGuess = False
					confirmed = False
					statUpdate = False
					wordSet = False
					confirm = False
					word = []
					clueWord = []
					wordLen = 0
					prompt = pygame.image.load('prompt.png')
					promptRect = prompt.get_rect()
					promptRect = promptRect.move([50, 50])
					basePromptRect = prompt.get_rect()
					basePromptRect = basePromptRect.move([50,50])
					statPrompt = pygame.image.load('statsPrompt.png')
					statPromptRect = statPrompt.get_rect()
					statPromptRect = statPromptRect.move([10, 10])
					guessPrompt = pygame.image.load('promptBase.png')
					guessPromptRect = guessPrompt.get_rect()
					guessPromptRect = guessPromptRect.move([10, 275])
					confirmGuessPrompt = pygame.image.load('promptConfirmGuess.png')
					CGPRect = confirmGuessPrompt.get_rect()
					CGPRect = CGPRect.move([10, 275])
	
	screen.fill(black)
	if winCondition:
		screen.blit(winScreen, winRect)
	elif loseCondition:
		screen.blit(loseScreen, loseRect)
	else:
		screen.blit(background, backRect)
		screen.blit(gallows, gallowsRect)
		
		promptText = ''.join(word)
		if(len(promptText) < 11):
			promptRect = pyFont.render_to(prompt, (110, 20), promptText, bgcolor=None, style=0, rotation=0, size=20)
		elif(len(promptText) > 10 and len(promptText) < 21):
			promptRect = pyFont.render_to(prompt, (110, 20), promptText[0:9], bgcolor=None, style=0, rotation=0, size=20)
			promptRect = pyFont.render_to(prompt, (10, 40), promptText[10:], bgcolor=None, style=0, rotation=0, size=20)
		else:
			promptRect = pyFont.render_to(prompt, (110, 20), promptText[0:9], bgcolor=None, style=0, rotation=0, size=20)
			promptRect = pyFont.render_to(prompt, (10, 40), promptText[10:29], bgcolor=None, style=0, rotation=0, size=20)
			promptRect = pyFont.render_to(prompt, (10, 60), promptText[29:], bgcolor=None, style=0, rotation=0, size=20)
			
			
		#Checks if a word has been set
		if(not wordSet):
			screen.blit(prompt, promptRect)
		else:
			if(wordLen == 0 or statUpdate):
				wordLen = len(word)
				statPrompt = pygame.image.load('statsPrompt.png')
				statPromptRect = statPrompt.get_rect()
				statPromptRect = statPromptRect.move([10, 10])
				statPromptRect = pyFont.render_to(statPrompt, (145, 25), str(wordLen - occurances), bgcolor=None, style=0,rotation=0, size=16)
				statPromptRect = pyFont.render_to(statPrompt, (145, 45), str(incorrectAttempts), bgcolor = None, style=0,rotation=0, size = 16)
				statPromptRect = pyFont.render_to(statPrompt, (145, 65), str(maxAttemptsLeft), bgcolor = None, style = 0, rotation = 0, size = 16)
				
				incorrectIndex = 0
				for l in incorrectGallery:
					if incorrectIndex < 10:
						statPromptRect = pyFont.render_to(statPrompt, (10 + ((incorrectIndex%10+2) * 16), 120), str(l + ' '), bgcolor=None, style=0, rotation=0, size=16)
					elif incorrectIndex < 20:
						statPromptRect = pyFont.render_to(statPrompt, (10 + ((incorrectIndex%10+2) * 16), 145), str(l + ' '), bgcolor=None, style=0, rotation=0, size=16)
					else:
						statPromptRect = pyFont.render_to(statPrompt, (10 + ((incorrectIndex%10+2) * 16), 170), str(l + ' '), bgcolor=None, style=0, rotation=0, size=16)
					incorrectIndex = incorrectIndex + 1
				statUpdate = False
			if(len(clueWord) == 0):
				for l in word:
					clueWord.append(False)
				wordIndex = 0
				for l in word:
					if l == ';' or l == ':' or l == '_' or l == ' ':
						clueWord[wordIndex] = True
						occurances = occurances + 1
					if clueWord[wordIndex] == True:
						guessPromptRect = pyFont.render_to(guessPrompt, (10+(25 * wordIndex), 25), word[wordIndex], bgcolor=None, style=0,rotation=0, size=24)
					else:
						guessPromptRect = pyFont.render_to(guessPrompt, (10+(25 * wordIndex), 25), '_ ', bgcolor=None, style=0,rotation=0, size=24)
					wordIndex = wordIndex + 1
				guessPromptRect = guessPromptRect.move([10, 275])
			
			if(not currentGuess == ':'):
				if confirmGuess == False:
					guessPrompt = confirmGuessPrompt
					guessPromptRect = CGPRect
					guessPromptRect = pyFont.render_to(guessPrompt, (210, 125), currentGuess, bgcolor=None, style=0, rotation=0,size = 24)
					guessPromptRect = guessPromptRect.move([10, 275])
				else:
					guessPrompt = pygame.image.load('promptBase.png')
					guessPromptRect = guessPrompt.get_rect()
					guessPromptRect = guessPromptRect.move([10, 275])
					
					wordIndex = 0
					for l in word:
						if l == currentGuess:
							clueWord[wordIndex] = True
							confirmed = True
							statUpdate = True
							occurances = occurances + 1
						if clueWord[wordIndex] == True:
							guessPromptRect = pyFont.render_to(guessPrompt, (10+(25 * wordIndex), 25), word[wordIndex], bgcolor=None, style=0,rotation=0, size=24)
						else:
							guessPromptRect = pyFont.render_to(guessPrompt, (10+(25 * wordIndex), 25), '_ ', bgcolor=None, style=0,rotation=0, size=24)
						guessPromptRect = guessPromptRect.move([10, 275])
						wordIndex = wordIndex + 1
					if(not confirmed):
						statUpdate = True
						maxAttemptsLeft = maxAttemptsLeft - 1
						incorrectAttempts = incorrectAttempts + 1
						incorrectGallery.append(currentGuess)
					else:
						confirmed = False
					confirmGuess = False
					currentGuess = ':'
					confirmGuessPrompt = pygame.image.load('promptConfirmGuess.png')
					CGPRect = confirmGuessPrompt.get_rect()
					CGPRect = CGPRect.move([10, 275])
					
					winCondition = True
					for c in clueWord:
						if c == False:
							winCondition = False
					
					if maxAttemptsLeft == 0:
						loseCondition = True
		
			screen.blit(statPrompt, statPromptRect)
			screen.blit(guessPrompt, guessPromptRect)
		
		if(maxAttemptsLeft < 6):
			screen.blit(headBasic, headRect)
		if(maxAttemptsLeft < 5):
			screen.blit(body, bodyRect)
		if(maxAttemptsLeft < 4):
			screen.blit(leftArm, leftARect)
		if(maxAttemptsLeft < 3):
			screen.blit(rightArm, rightARect)
		if(maxAttemptsLeft < 2):
			screen.blit(leftLeg, leftLRect)
		if(maxAttemptsLeft < 1):
			screen.blit(rightLeg, rightLRect)
	pygame.display.flip()