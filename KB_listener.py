from pynput.keyboard import Key, KeyCode, Listener

def get_key_type(key):
    k = key

    if key == Key.ctrl_l:
        k = 'ctrl_l'

    elif key == Key.ctrl_r:
        k = 'ctrl_r'

    elif key == Key.alt_l:
        k = 'alt_l'

    elif key == Key.alt_r:
        k = 'alt_r'

    elif key == Key.backspace:
        k = 'backspace'

    elif key == Key.caps_lock:
        k = 'caps_lock'

    elif key == Key.cmd_l:
        k = 'cmd_l'

    elif key == Key.cmd_r:
        k = 'cmd_r'

    elif key == Key.delete:
        k = 'delete'

    elif key == Key.end:
        k = 'end'

    elif key == Key.down:
        k = 'down'

    elif key == Key.enter:
        k = 'enter'

    elif key == Key.esc:
        k = 'esc'

    elif key == Key.f1:
        k = 'f1'

    elif key == Key.f2:
        k = 'f2'

    elif key == Key.f3:
        k = 'f3'

    elif key == Key.f4:
        k = 'f4'

    elif key == Key.f5:
        k = 'f5'

    elif key == Key.f6:
        k = 'f6'

    elif key == Key.f7:
        k = 'f7'

    elif key == Key.f8:
        k = 'f8'

    elif key == Key.f9:
        k = 'f9'

    elif key == Key.f10:
        k = 'f10'

    elif key == Key.f11:
        k = 'f11'

    elif key == Key.f12:
        k = 'f12'

    elif key == Key.f13:
        k = 'f13'

    elif key == Key.f14:
        k = 'f14'

    elif key == Key.f15:
        k = 'f15'

    elif key == Key.f16:
        k = 'f16'

    elif key == Key.f17:
        k = 'f17'

    elif key == Key.f18:
        k = 'f18'

    elif key == Key.f19:
        k = 'f19'

    elif key == Key.f20:
        k = 'f20'

    elif key == Key.home:
        k = 'home'

    elif key == Key.left:
        k = 'left'

    elif key == Key.page_down:
        k = 'page_down'

    elif key == Key.page_up:
        k = 'page_up'

    elif key == Key.right:
        k = 'right'

    elif key == Key.shift_l:
        k = 'shift_l'

    elif key == Key.shift_r:
        k = 'shift_r'

    elif key == Key.space:
        k = 'space'

    elif key == Key.tab:
        k = 'tab'

    elif key == Key.up:
        k = 'up'

    elif key == Key.insert:
        k = 'insert'

    elif key == Key.num_lock:
        k = 'num_lock'

    elif key == Key.print_screen:
        k = 'print_screen'

    elif key == Key.scroll_lock:
        k = 'scroll_lock'

    elif key.char == '\x03':
        k = 'ctrl + c'

    elif key.char == '\x16':
        k = 'ctrl + v'

    return k


def on_press(key):  
    k = get_key_type(key)
    print('{0} pressed'.format(k))

def on_release(key):
    k = get_key_type(key)
    print('{0} release'.format(k))

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
