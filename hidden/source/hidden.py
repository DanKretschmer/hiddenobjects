import pygame
from pygame.mask import from_surface
import os
import sys


pygame.init()
pygame.mixer.init()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


background_music_path = resource_path("music.mp3")
pygame.mixer.music.load(background_music_path)
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely.
pygame.mixer.music.set_volume(0.2)  # Set the volume of the music


WIDTH, HEIGHT = 600, 600
DISPLAY_TIME = 3 * 1000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND = pygame.image.load("images/screen1.jpg")
WIN_BACKGROUND = pygame.image.load("images/win.jpg")
SCROLL_BOX_FONT = pygame.font.Font(None, 20)
FONT = pygame.font.Font(None, 20)
TITLE_IMAGE = pygame.image.load("images/title.jpg")


CORRECT_SOUND = pygame.mixer.Sound(resource_path("sounds/ding.mp3"))
WRONG_SOUND = pygame.mixer.Sound(resource_path("sounds/wrong.mp3"))
CORRECT_SOUND.set_volume(1.0)  
WRONG_SOUND.set_volume(1.0) 


levels_data = {
    1: {
    'background': pygame.image.load(resource_path("images/screen1.jpg")),
    'objects': {
    'a lute': {
        #'image': pygame.image.load("images/lute.png"),
        'image': pygame.image.load(resource_path("images/lute.png")),
        'clicked_image': pygame.image.load(resource_path("images/lute_clicked.png")),
        'coords': (550, 200),
        'found': False
    },
    'pears': {
        'image': pygame.image.load(resource_path("images/pears.png")),
        'clicked_image': pygame.image.load(resource_path("images/pears_clicked.png")),
        'coords': (150, 150),
        'found': False
    },
   'hidden elephant': {
        'image': pygame.image.load(resource_path("images/elephant.png")),
        'clicked_image': pygame.image.load(resource_path("images/elephant_clicked.png")),
        'coords': (0, 130),
        'found': False
    },
    'a bird eating': {
        'image': pygame.image.load(resource_path("images/birdeating.png")),
        'clicked_image': pygame.image.load(resource_path("images/birdeating_clicked.png")),
        'coords': (260, 50),
        'found': False
    },
    'owl': {
        'image': pygame.image.load(resource_path("images/owl.png")),
        'clicked_image': pygame.image.load(resource_path("images/owl_clicked.png")),
        'coords': (528, 55),
        'found': False
    },
    'hidden lion': {
        'image': pygame.image.load(resource_path("images/lion.png")),
        'clicked_image': pygame.image.load(resource_path("images/lion_clicked.png")),
        'coords': (150, 450),
        'found': False
    },
    'the sun': {
        'image': pygame.image.load(resource_path("images/sun.png")),
        'clicked_image': pygame.image.load(resource_path("images/sun_clicked.png")),
        'coords': (450, 63),
        'found': False
    }
        }
    },
    2: {
    'background': pygame.image.load(resource_path("images/screen2.jpg")),
    'objects': {
         'a green bottle': {
        'image': pygame.image.load(resource_path("images/greenbottle.png")),
        'clicked_image': pygame.image.load(resource_path("images/greenbottle_clicked.png")),
        'coords': (500, 75),
        'found': False
    },
    'white dove': {
        'image': pygame.image.load(resource_path("images/whitedove.png")),
        'clicked_image': pygame.image.load(resource_path("images/whitedove_clicked.png")),
        'coords': (242, 115),
        'found': False
    },
   "man's face": {
        'image': pygame.image.load(resource_path("images/manface.png")),
        'clicked_image': pygame.image.load(resource_path("images/manface_clicked.png")),
        'coords': (294, 442),
        'found': False
    },
    'monkey with a back scratcher': {
        'image': pygame.image.load(resource_path("images/monkeyscratcher.png")),
        'clicked_image': pygame.image.load(resource_path("images/monkeyscratcher_clicked.png")),
        'coords': (117, 146),
        'found': False
    },
    'coffee pitcher': {
        'image': pygame.image.load(resource_path("images/coffeepitcher.png")),
        'clicked_image': pygame.image.load(resource_path("images/coffeepitcher_clicked.png")),
        'coords': (0, 230),
        'found': False
    },
    'flute': {
        'image': pygame.image.load(resource_path("images/flute.png")),
        'clicked_image': pygame.image.load(resource_path("images/flute_clicked.png")),
        'coords': (112, 470),
        'found': False
    },
    'paint palette': {
        'image': pygame.image.load(resource_path("images/palette.png")),
        'clicked_image': pygame.image.load(resource_path("images/palette_clicked.png")),
        'coords': (517, 355),
        'found': False
    }
        }
    },
    3: {
    'background': pygame.image.load(resource_path("images/screen3.jpg")),
    'objects': {
    'an upside down bottle': {
        'image': pygame.image.load(resource_path("images/upsidedownbottle.png")),
        'clicked_image': pygame.image.load(resource_path("images/upsidedownbottle_clicked.png")),
        'coords': (310, 470),
        'found': False
    },
    'back scratcher': {
        'image': pygame.image.load(resource_path("images/backscratcher2.png")),
        'clicked_image': pygame.image.load(resource_path("images/backscratcher2_clicked.png")),
        'coords': (230, 400),
        'found': False
    },
   'rabbit': {
        'image': pygame.image.load(resource_path("images/rabbit.png")),
        'clicked_image': pygame.image.load(resource_path("images/rabbit_clicked.png")),
        'coords': (0, 150),
        'found': False
    },
    'secret monkey': {
        'image': pygame.image.load(resource_path("images/hiddenmonkey.png")),
        'clicked_image': pygame.image.load(resource_path("images/hiddenmonkey_clicked.png")),
        'coords': (96, 385),
        'found': False
    },
    'striped cat': {
        'image': pygame.image.load(resource_path("images/cat.png")),
        'clicked_image': pygame.image.load(resource_path("images/cat_clicked.png")),
        'coords': (400, 350),
        'found': False
    },
    'person playing a flute': {
        'image': pygame.image.load(resource_path("images/fluteplayer.png")),
        'clicked_image': pygame.image.load(resource_path("images/fluteplayer_clicked.png")),
        'coords': (500, 450),
        'found': False
    },
    'bird': {
        'image': pygame.image.load(resource_path("images/bird.png")),
        'clicked_image': pygame.image.load(resource_path("images/bird_clicked.png")),
        'coords': (375, 73),
        'found': False
    }
        }
    }
}
    

WIN_CONDITION = sum(len(data['objects']) for data in levels_data.values())
current_level = 1
objects_data = {}
levels = [objects_data]
wrong_click_timer = 0


for key, data in objects_data.items():
    if data['image']:
        data['mask'] = from_surface(data['image'])


def check_collision(object_key, x, y):
    obj = objects_data[object_key]
    obj_x, obj_y = obj['coords']
    if (obj_x <= x <= obj_x + obj['image'].get_width() and
            obj_y <= y <= obj_y + obj['image'].get_height()):
        if obj['mask'].get_at((int(x - obj_x), int(y - obj_y))) and not obj['found']:
            obj['found'] = True
            return True
    return False


def load_level(level):
    global objects_data, BACKGROUND  
    objects_data = levels_data[level]['objects']
    BACKGROUND = levels_data[level]['background']
    for key, data in objects_data.items():
        if data['image']:
            data['mask'] = from_surface(data['image'])


# Initially, load the first level:
load_level(current_level)


def wrap_text(text, FONT, max_width):
    words = text.split(' ')
    wrapped_lines = []
    line = ''

    for word in words:
        test_line = line + word + ' '
        width, _ = SCROLL_BOX_FONT.size(test_line)
        if width <= max_width:
            line = test_line
        else:
            wrapped_lines.append(line)
            line = word + ' '
    wrapped_lines.append(line)
    
    return wrapped_lines

def get_scroll_box_text(level):
    base_text = "Find these: "
    full_text = "Find these: " + ", ".join([key for key in levels_data[level]['objects'].keys()])
    return wrap_text(full_text, SCROLL_BOX_FONT, WIDTH)


title_displayed = True
start_time_title = pygame.time.get_ticks()


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hidden Object Game")
    global current_level
   
    #SCROLL_BOX_FONT = pygame.font.Font(None, 20)
    scroll_box_texts = get_scroll_box_text(current_level)
    title_displayed = True
    start_time_title = pygame.time.get_ticks()
    while title_displayed and pygame.time.get_ticks() - start_time_title < DISPLAY_TIME:
        screen.blit(TITLE_IMAGE, (0, 0))
        pygame.display.flip()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    end_time = None
    scroll_box_rect = pygame.Rect(0, 0, WIDTH, 30)
    wrong_click_text = ""
    number_of_wrong_guesses = 0
    total_items_found = 0


    game_state = "playing"
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time_title < 3000:
        screen.blit(TITLE_IMAGE, (0, 0))
        pygame.display.flip()


    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_state == "playing":
                x, y = event.pos
                
                
                for object_key in objects_data:
                    if check_collision(object_key, x, y):
                        total_items_found += 1
                        CORRECT_SOUND.play()
                        break
                else:
                    wrong_click_text = "Nothing there!"
                    number_of_wrong_guesses += 1
                    wrong_click_timer = pygame.time.get_ticks()
                    WRONG_SOUND.play()

        if game_state == "won":
            screen.blit(WIN_BACKGROUND, (0, 0))

            elapsed_time_in_seconds = (end_time - start_time) / 1000  # Convert milliseconds to seconds
            
            minutes = int(elapsed_time_in_seconds // 60)
            seconds = int(elapsed_time_in_seconds % 60)


            win_text = "You found them all! "
            if number_of_wrong_guesses != 1:
                 win_text += f"You made {number_of_wrong_guesses} wrong guesses."
            else:
                win_text += "You made 1 wrong guess. "
            
            if minutes != 1:
                win_text += f" It took you {minutes} minutes and {seconds} seconds."
            else:
                win_text += f" It took you 1 minute and {seconds} seconds."
            
      
            text_surface = FONT.render(win_text, True, WHITE)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)
            pygame.display.flip()
            continue

        
        if total_items_found == len(levels_data[current_level]['objects']):
           
            current_level += 1
            total_items_found = 0
            if current_level > len(levels_data):
                game_state = "won"
                end_time = pygame.time.get_ticks()
                continue
            else:
                load_level(current_level)
                scroll_box_texts = get_scroll_box_text(current_level)
              
    
        screen.blit(BACKGROUND, (0, 0))
        for object_key, data in objects_data.items():   
            x, y = data['coords']
            if data['image'] and not data['found']:
                screen.blit(data['image'], (x, y))
            elif data['clicked_image'] and data['found']:
                screen.blit(data['clicked_image'], (x, y))

        if wrong_click_text:
            current_time = pygame.time.get_ticks()
            if current_time - wrong_click_timer >= DISPLAY_TIME:
                wrong_click_text = ""

            text = FONT.render(wrong_click_text, True, WHITE)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 20))
            screen.blit(text, text_rect)

        
        pygame.draw.rect(screen, BLACK, scroll_box_rect)

        y_offset = 5
        for line in scroll_box_texts:
            scroll_box_surface = SCROLL_BOX_FONT.render(line, True, WHITE)
            screen.blit(scroll_box_surface, (10, y_offset))
            y_offset += SCROLL_BOX_FONT.get_height()


        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
