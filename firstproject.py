return playerHP
					
#define secondFight
#antiquated, needs to be replaced with general fight function
def swampFight(exp,playerHP):
	hp=100
	attack = exp
	guess =None
	i=0
		
	while hp>=1:
		luck=0
		maxi= i+2
		guess =int(input('Guess the number between 1 and %g:\n'%maxi))
		if guess == random.randint(1,2+i):
			print('Nice! You feel stronger and more accurate as you attack.')
			i+=1
			luck=guess
		accuracy =random.randint(1,10)+exp+luck
		#start attack
		if accuracy >= 3:
			print(name+' got a succesful hit! You did ' +str(attack+luck)+ ' damage!')
			hp-=attack+luck
			if hp>=1:
				print('\n Current enemy hp is %g.\n' %hp)
			else:
				print('\n Enemy defeated. You gain 1 exp. \n')
		elif luck == 1:
			print('...but you missed anyway')
		else:
			playerHP -=30
			print ('Missed attack...you take 30 damage')
		if playerHP ==0:
			print('Your journey ends here')

			
	#Navigate
		
while exp <= 10:
	if playerHP <=0:
		break
	direction= input('Go where?\n')
	
	if direction == 'rest':
		if gold >=1: 
			gold-=1
			print('You spend gold and rest. You gain ' +str(10-playerHP)+' HP')
		else:
			print('You have no gold.')
			
	if direction == 'field' or direction =='f':
		print('Field Fight start, current exp is %g.' %exp)
		playerHP=fieldFight(exp,playerHP)
		exp+=1	
		
	if direction == 'swamp' or direction == 's':
		swampFight(exp,playerHP)
		exp+=0
	
	if direction == 'check':
		print(playerHP,gold)
		
	if direction == 'help':
		print('you can type check, swamp, field, and;rest')

print('GAME	HAS	ENDED')
