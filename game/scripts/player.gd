extends CharacterBody2D

@export var speed = 300
var click_pos = Vector2()
var target_pos = Vector2()

func _ready():
	click_pos = position
	
func _physics_process(delta):
	if Input.is_action_just_pressed("left_click"):
		click_pos = get_global_mouse_position()
		
	if position.distance_to(click_pos) > 3:
		target_pos = (click_pos - position).normalized()
		velocity = target_pos * speed
		if click_pos.x > position.x:
			$AnimatedSprite2D.flip_h = false
			$AnimatedSprite2D.play("walk")
			move_and_slide()
		else:
			$AnimatedSprite2D.flip_h = true
			$AnimatedSprite2D.play("walk")
			move_and_slide()
