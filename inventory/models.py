from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import Group







class InventoryItem(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	quantity = models.IntegerField()
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	specific_backup = models.IntegerField(default=5)
	status = models.ForeignKey('Status', on_delete=models.SET_NULL, blank=True, null=True)
	label = models.CharField(max_length=200, null=True, blank=True)
	supplier = models.CharField(max_length=200, null=True, blank=True)
	room = models.ForeignKey('Room', on_delete=models.SET_NULL, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
	date_modified = models.DateTimeField(auto_now=True,null=True, blank=True)
	serial = models.CharField(max_length=200, null=True, blank=True)
	local = models.CharField(max_length=200, null=True, blank=True)
	model = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to='item_images/', null=True, blank=True)  # New field for the image
	requirement_las_vegas = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_las_vegas = models.CharField(max_length=200, null=True, blank=True)
	requirement_abu_dhabi = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_abu_dhabi = models.CharField(max_length=200, null=True, blank=True)
	requirement_monaco = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_monaco = models.CharField(max_length=200, null=True, blank=True)
	requirement_suzuka = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_suzuka = models.CharField(max_length=200, null=True, blank=True)
	requirement_ph_studio = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_ph_studio = models.CharField(max_length=200, null=True, blank=True)
	requirement_3d_dept = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_3d_dept = models.CharField(max_length=200, null=True, blank=True)
	requirement_seven_floor = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_seven_floor = models.CharField(max_length=200, null=True, blank=True)
	requirement_mini_pitx = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_mini_pitx = models.CharField(max_length=200, null=True, blank=True)
	requirement_plinko = models.CharField(max_length=200, null=True, blank=True)
	propose_spare_plinko = models.CharField(max_length=200, null=True, blank=True)




	c1_requirement_las_vegas = models.CharField(max_length=200, null=True, blank=True)
	c1_propose_spare_las_vegas = models.CharField(max_length=200, null=True, blank=True)
	c2_requirement_abu_dhabi = models.CharField(max_length=200, null=True, blank=True)
	c2_propose_spare_abu_dhabi = models.CharField(max_length=200, null=True, blank=True)
	c4_requirement_monaco = models.CharField(max_length=200, null=True, blank=True)
	c4_propose_spare_monaco = models.CharField(max_length=200, null=True, blank=True)
	c3_requirement_suzuka = models.CharField(max_length=200, null=True, blank=True)
	c3_propose_spare_suzuka = models.CharField(max_length=200, null=True, blank=True)
	it_room_requirements = models.CharField(max_length=200, null=True, blank=True)
	it_room_propose_spare = models.CharField(max_length=200, null=True, blank=True)
	it_room_storage_requirement = models.CharField(max_length=200, null=True, blank=True)
	it_room_storage_propose_spare = models.CharField(max_length=200, null=True, blank=True)
	storage_1_requirement = models.CharField(max_length=200, null=True, blank=True)
	storage_1_propose_spare = models.CharField(max_length=200, null=True, blank=True)
	admin_hr_requirement = models.CharField(max_length=200, null=True, blank=True)
	admin_hr_propose_spare = models.CharField(max_length=200, null=True, blank=True)
	hallway_requirement = models.CharField(max_length=200, null=True, blank=True)
	hallway_propose_spare = models.CharField(max_length=200, null=True, blank=True)
	commentator_pantry_requirement = models.CharField(max_length=200, null=True, blank=True)
	commentator_pantry_propose_spare = models.CharField(max_length=200, null=True, blank=True)

	groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='inventory_items')

	def __str__(self):
		return self.name


	class Meta:
		ordering = ['-date_created']

class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # Describe the action, e.g., 'Updated Item', 'Deleted Item'
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, null=True, blank=True)  # You can link it to inventory items if needed
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"


from django.db import models
from django.contrib.auth.models import User, Group
from django.conf import settings


# Assuming InventoryItem and Room models are defined elsewhere

class SpecificItem(models.Model):
	STATUS_CHOICES = [
		('inUse', 'In Use'),
		('readyForDeployment', 'Ready for Deployment'),
		('backup/Stock', 'Backup/Stock'),
		('orderedWaitingForShipment', 'Order waiting for shipment'),
		('requested,NotYetPlaceOrder', 'Requested,not yet place order'),
		('broken', 'Broken'),
		('resell', 'Resell'),
	]

	STATUS_COLORS = {
		'inUse': '#03fc2c',
		'readyForDeployment': '#47abd6',
		'backup/Stock': '#d1bc34',
		'orderedWaitingForShipment': '#a89274',
		'requested,NotYetPlaceOrder': '#b58353',
		'broken': '#757c80',
		'resell': '#f21818',
	}

	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='None')
	inventory_item = models.ForeignKey('InventoryItem', related_name='specific_items', on_delete=models.CASCADE)

	added_by = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='created_specific_items'  # Add this
	)

	quantity_added = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	label = models.CharField(max_length=100, blank=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

	last_modified_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='modified_specific_items'  # Add this
	)

	room = models.ForeignKey('Room', on_delete=models.SET_NULL, blank=True, null=True)
	groups = models.ManyToManyField(Group)
	serial = models.CharField(max_length=200, null=True, blank=True)
	model = models.CharField(max_length=200, null=True, blank=True)
	details = models.CharField(max_length=200, null=True, blank=True)

	def get_status_color(self):
		return self.STATUS_COLORS.get(self.status, '#ffffff')  # Default to white

	def __str__(self):
		return f"{self.inventory_item.name} - {self.id}"






class Category(models.Model):
	name = models.CharField(max_length=200)
	color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code

	class Meta:
		verbose_name_plural = 'categories'


	def __str__(self):
		return self.name


class Status(models.Model):
	name = models.CharField(max_length=100)
	color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code
	class Meta:
		verbose_name_plural = 'status'

	def __str__(self):
		return self.name



class Room(models.Model):

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='none')

    class Meta:
        verbose_name_plural = 'rooms'

    def __str__(self):
        return self.name

class TransactionLog(models.Model):


    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.action} by {self.user.username} on {self.timestamp}'


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Lasvegas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    topview = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    network_status = models.CharField(max_length=50,default="GOOD")
    printer_status = models.CharField(max_length=50,default="GOOD")
    AI_Cam = models.CharField(max_length=50,default="GOOD")

class Monaco(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    topview = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    network_status = models.CharField(max_length=50,default="GOOD")
    printer_status = models.CharField(max_length=50,default="GOOD")
    AI_Cam = models.CharField(max_length=50,default="GOOD")
class Suzuka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    topview = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    network_status = models.CharField(max_length=50,default="GOOD")
    printer_status = models.CharField(max_length=50,default="GOOD")
    AI_Cam = models.CharField(max_length=50,default="GOOD")
class Abudhabi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    topview = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    network_status = models.CharField(max_length=50,default="GOOD")
    printer_status = models.CharField(max_length=50,default="GOOD")
    AI_Cam = models.CharField(max_length=50,default="GOOD")



class Philippines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    topview = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    network_status = models.CharField(max_length=50,default="GOOD")
    printer_status = models.CharField(max_length=50,default="GOOD")
    AI_Cam = models.CharField(max_length=50,default="GOOD")




class Plinko(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    topview = models.CharField(max_length=50)
    obs = models.CharField(max_length=50)
    audio = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    network_status = models.CharField(max_length=50,default="GOOD")
    printer_status = models.CharField(max_length=50,default="GOOD")
    AI_Cam = models.CharField(max_length=50,default="GOOD")




from django.db import models
from django.contrib.auth.models import User


class Obstacle(models.Model):
	STUDIO_CHOICES = [
		('las_vegas', 'Las Vegas'),
		('monaco', 'Monaco'),
		('suzuka', 'Suzuka'),
		('abudhabi', 'Abu Dhabi'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	studio = models.CharField(max_length=20, choices=STUDIO_CHOICES)
	file = models.FileField(upload_to='obstacles/')
	image = models.ImageField(upload_to='obstacle_images/', null=True, blank=True)  # Image field
	details = models.TextField(null=True, blank=True)

	uploaded_at = models.DateTimeField(auto_now_add=True)

	def filename(self):
		return self.file.name.split('/')[-1]

	def __str__(self):
		return f"Obstacle at {self.studio} by {self.user.username}"


# inventory/models.py
from django.db import models
from django.contrib.auth.models import User

class ChecklistSubmission(models.Model):
    studio = models.CharField(max_length=100)
    equipment_name = models.CharField(max_length=100)
    checked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    check_time = models.TimeField()
    check_date = models.DateField()
    status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    submission_group_id = models.CharField(max_length=50, help_text="Identifier to group all items from a single submission")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipment_name} on {self.check_date} by {self.checked_by}"