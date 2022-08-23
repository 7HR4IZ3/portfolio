import inspect
from datetime import date
import random
from sqlite import SqliteDatabase
db = SqliteDatabase("database.sqlite", check_same_thread=False)

class DBPlugin:
	name = "dbplugin"
	api = 2

	def __init__(self, db):
		self.db = db

	def apply(self, callback, route):
		if "table" not in inspect.getfullargspec(callback)[0]:
			return callback

		def wrapper(*a, **kw):
			kw["table"] = self.db.models[kw["table"].title()]
			return callback(*a, **kw)
		return wrapper

class Posts(db.Model):
	author_id = db.Column("integer", default=1)
	title = db.Column(null=False)
	image = db.Column()
	date = db.Column("date")
	body = db.Column(null=False)
	category = db.Column(default="")
	tag = db.Column(default="")
	rating = db.Column("integer", default=1)

class Author(db.Model):
	name = db.Column()
	image = db.Column()

class Messages(db.Model):
	
	name = db.Column(null=False)
	email = db.Column(null=False)
	website = db.Column()
	value = db.Column(null=False)

class Replies(Messages):
	message_id = db.Column("integer")

class Plans(db.Model):
	title = db.Column()
	icon_cls = db.Column()
	detail = db.Column()
	price = db.Column()
	period =db.Column(default="monthly")
	rating = db.Column("integer")

class Testimonials(db.Model):
	name = db.Column()
	image = db.Column()
	value = db.Column()
	status = db.Column()

class Services(db.Model):
	name = db.Column()
	icon = db.Column()
	detail = db.Column()

db.init(Posts, Plans, Author, Messages, Replies, Testimonials, Services)

posts = Posts()
plans = Plans()
author = Author()
messages = Messages()
testimonials = Testimonials()
services = Services()


def demo():
	author.new({
		"name": "Demian Thraize",
		"image": "person_1.jpg"
	})
	author.new({
		"name": "Ian Thraize",
		"image": "person_1.jpg"
	})
	posts.new({
		"title": "Brython vs pyscript",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	posts.new({
		"title": "Top 3 web frameworks",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	posts.new({
		"title": "Django or flask",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	posts.new({
		"title": "Wsgi vs Asgi",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	posts.new({
		"title": "Python for web-dev",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	posts.new({
		"title": "Django or flask part2",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	posts.new({
		"title": "Wsgi vs Asgi part2",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	posts.new({
		"title": "Python for web-dev part2",
		"image": "", 
		"date": date(2022, 5, 17),
		"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
		"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
		"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
		"rating": "4"
	})
	for i in range(100):
		posts.new({
			"title": "dummy post number %i on index %i" %(random.randint(0, 500), 60+i),
			"date": date.today(),
			"category": "LifeStyle, Food, Healthy, Sports, Entertainment",
			"tag": "Projects, Design, Travel, Brand, Trending, Knowledge, Food",
			"body": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!/nl/Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum, ratione quidem. Neque distinctio nulla optio adipisci perferendis beatae, voluptas delectus quae corrupti natus hic voluptates ipsum repellat asperiores architecto exercitationem!",
			"rating": "%i"%random.randint(0, 5)
		})
	plans.new({
		"title": "Membership",
		"icon_cls": "mai-people",
		"detail": "Choose the plan that right for you",
		"price": "30",
		"rating": 2
	})
	plans.new({
		"title": "Dedicated",
		"icon_cls": "mai-business",
		"detail": "Choose the plan that right for you",
		"price": "60",
		"rating": 5
	})
	plans.new({
		"title": "Private",
		"icon_cls": "mai-rocket-outline",
		"detail": "Choose the plan that right for you",
		"price": "90",
		"rating": 2
	})
	testimonials.new({
		"image": "person_1.jpg",
		"value": "Necessitatibus ipsum magni accusantium consequatur delectus a repudiandae nemo quisquam dolorum itaque, tenetur, esse optio eveniet beatae explicabo sapiente quo.",
		"name": "Melvin Platje",
		"status": "CEO Slurin Group"
	})
	testimonials.new({
		"image": "person_2.jpg",
		"value": "Repudiandae vero assumenda sequi labore ipsum eos ducimus provident a nam vitae et, dolorum temporibus inventore quaerat consectetur quos! Animi, qui ratione?",
		"name": "George Burke",
		"status": "CEO Letro"
	})
	services.new({
		"name": "High Performance",
		"icon": "mai-shapes",
		"detail":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, sit."
	})
	services.new({
		"name": "Friendly Prices",
		"icon": "mai-shapes",
		"detail":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, sit."
	})
	services.new({
		"name": "No time-confusing",
		"icon": "mai-shapes",
		"detail":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, sit."
	})
