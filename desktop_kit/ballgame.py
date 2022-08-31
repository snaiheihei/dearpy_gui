import random
import time
from aip_speech_text import get_speech_from_text
import soundAPI
import pygame
import os

class Jieqiu(object):

	def __init__(self):
		folder = os.path.dirname(os.path.abspath("__file__"))
		# 初始化背景音乐, 方式一 pygame mixer播放，支持多类型音频
		theme_file = os.path.join(folder, "sound", '人生最美初见时.mp3')
		soundAPI.music_effectsDispatcher(theme_file)
		# 初始化背景音乐, 方式二 playsound2播放，支持音频少，轻量化
		# theme_file = os.path.join(folder, "sound", 'theme.mp3')
		# soundAPI.audio_effectsDispatcher(theme_file)

		#初始化pygamee
		pygame.init()
		game_window=pygame.display.set_mode((600,500))
		pygame.display.set_caption('接球')
		window_color = (0,0,255)

		ball_color=(255,165,0)
		rect_color=(255,0,0)
		ball_x = random.randint(20,580)
		ball_y = 20

		score = 0
		font=pygame.font.Font(None,70)

		move_x = 1
		move_y = 1

		point=1
		count =1
		while True:

			game_window.fill(window_color)
			for event in pygame.event.get():
				# print(event)
				if event.type==pygame.QUIT:
					sys.exit()
			mouse_x,mouse_y = pygame.mouse.get_pos()

			pygame.draw.circle(game_window,ball_color,(ball_x,ball_y),20)
			pygame.draw.rect(game_window,rect_color,(mouse_x,490,100,8))
			# 显示字体
			my_text=font.render(str(score),False,(255,253,233))
			game_window.blit(my_text,(500,30))
			#更新
			ball_x+=move_x
			ball_y+=move_y
			time.sleep(0.008)

			if ball_x <= 20 or ball_x >= 580 :
				move_x=-move_x
				
			if ball_y <=20 :
				move_y= -move_y
			
			elif mouse_x-20 < ball_x <mouse_x+120 and ball_y>=470 :
				move_y= -move_y	
				score += point
				count+=1
				if count == 3:
					count = 0
					point+=point
					#向右移动 步进加1
					if move_x>0:
						move_x+=1
					#向左移动 步进加1	
					else:
						move_x-=1
					#球一定是向下落的 y步进加1
					move_y-=1
			elif ball_y>=480 and (ball_x<=mouse_x-20 or ball_x>=mouse_x+120):
				self.result = '您的游戏得分为%s分'%str(score)
				folder = os.path.dirname(os.path.abspath("__file__"))
				gameOver_file = os.path.join(folder, "sound", 'gameover.wav')
				soundAPI.audio_effectsDispatcher(gameOver_file)
				time.sleep(2)
				break
			pygame.display.update()

	def final_score(self):
			print(self.result)
			get_speech_from_text(self.result)
			

if __name__ == '__main__':
	jieqiu=Jieqiu()
	# jieqiu.final_score()


