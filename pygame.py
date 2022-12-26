running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update game state

    # Draw game objects
    pygame.display.flip()
