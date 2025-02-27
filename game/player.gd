extends Node2D

@export var speed = 400
# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	var velocity = Vector2.ZERO
	if Input.is_action_pressed("w"):
		velocity.y += 1
	if Input.is_action_pressed("s"):
		velocity.y -= 1
	if Input.is_action_pressed("a"):
		velocity.x -= 1
	if Input.is_action_pressed("d"):
		velocity.x += 1
	if velocity.length() > 0:
		velocity = velocity.normalized() * speed
	position += velocity * delta	
