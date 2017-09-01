from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, Base, Item, User
 
engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. 
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#Category1
category1 = Category(user_id = 1,name = "Soccer")

session.add(category1)
session.commit()

# Items under Soccer category
item1 = Item(user_id = 1, name = "Shinguards", description = "A piece of equipment worn on the front of a player's shin to protect them from injury", category = category1);

session.add(item1)
session.commit()

item2 = Item(user_id = 1, name = "Jersey", description = "A uniform that a sports team wear ", category = category1);

session.add(item2)
session.commit()

item3 = Item(user_id = 1, name = "Soccer Cleats", description = "Cleats or studs are protrusions on the sole of a shoe, or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface. They can be conical or blade-like in shape, and made of plastic, rubber or metal. In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions", category = category1);

session.add(item3)
session.commit()

#Category2
category2 = Category(user_id = 1,name = "Snowboarding")

session.add(category2)
session.commit()

# Items under Snowboarding category
item1 = Item(user_id = 1, name = "Snowboard", description = "Snowboards are boards that are usually the width of one's foot longways, with the ability to glide on snow.[1] Snowboards are differentiated from monoskis by the stance of the user. In monoskiing, the user stands with feet inline with direction of travel (facing tip of monoski/downhill) (parallel to long axis of board), whereas in snowboarding, users stand with feet transverse (more or less) to the longitude of the board. Users of such equipment may be referred to as snowboarders", category = category2);

session.add(item1)
session.commit()

item2 = Item(user_id = 1, name = "Boots", description = " Snowboard boots are mostly considered soft boots, though alpine snowboarding uses a harder boot similar to a ski boot. A boot's primary function is to transfer the rider's energy into the board, protect the rider with support, and keep the rider's feet warm. A snowboarder shopping for boots is usually looking for a good fit, flex, and looks. Boots can have different features such as lacing styles, heat molding liners, and gel padding that the snowboarder also might be looking for. Tradeoffs include rigidity versus comfort, and built in forward lean, versus comfort", category = category2);

session.add(item2)
session.commit()

#Category3
category3 = Category(user_id = 1,name = "Hockey")

session.add(category3)
session.commit()

item1 = Item(user_id = 1, name = "Stick", description = " A hockey stick is a piece of equipment used by the players in most forms of hockey to move the ball or puck.", category = category3);

session.add(item1)
session.commit()



