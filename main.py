import cocos

cocos.director.director.init( width=400, height=600, caption="My caption.", fullscreen=False )
		
class KeyDisplay(cocos.layer.Layer):

	is_event_handler = True
	
	def __init__(self):
		super( KeyDisplay, self ).__init__()
	
	def on_key_press (self, key, modifiers):
		print(key)
	
	def on_mouse_press (self, x, y, buttons, modifiers):
		distance=max( abs(x-hero.x) , abs(y-hero.y) )
		time=distance / 40
		move = cocos.actions.MoveBy((x-hero.x, y-hero.y), time)
		hero.do(move)
		
scene = cocos.scene.Scene(KeyDisplay())

hero=cocos.sprite.Sprite('b.PNG');

for row in range(20):
	for col in range(20):
		cell=cocos.sprite.Sprite('h.PNG',(row*31,col*31));
		scene.add( cell )
		
scene.add( hero )
cocos.director.director.show_FPS=True
cocos.director.director.run(scene)
