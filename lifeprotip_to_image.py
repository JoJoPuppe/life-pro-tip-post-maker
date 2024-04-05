from create_text import Post
from meme_extractor import LifeProTip

life_pro_tip = LifeProTip()
new_subs = life_pro_tip.get_lpt()

print(new_subs)

path = "./LTP_Posts/"

post = Post(500, path)
post.combine_gradient_and_text("Ujs jshd jsjjajajaks jhsjjs jshde jsdr")
post.show()
