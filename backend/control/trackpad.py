import Quartz.CoreGraphics as CG

def move_mouse(x: float, y: float):
    """
    Move the mouse to the coordinates (x, y).
    """
    move_event = CG.CGEventCreateMouseEvent(
        None,
        CG.kCGEventMouseMoved,
        (x, y),
        CG.kCGMouseButtonLeft
    )
    CG.CGEventPost(CG.kCGHIDEventTap, move_event)

def click_mouse(x: float, y: float):
    """
    Simulate a left-click at the coordinates (x, y).
    """
    move_mouse(x, y)
    mouse_down = CG.CGEventCreateMouseEvent(
        None,
        CG.kCGEventLeftMouseDown,
        (x, y),
        CG.kCGMouseButtonLeft
    )
    mouse_up = CG.CGEventCreateMouseEvent(
        None,
        CG.kCGEventLeftMouseUp,
        (x, y),
        CG.kCGMouseButtonLeft
    )
    CG.CGEventPost(CG.kCGHIDEventTap, mouse_down)
    CG.CGEventPost(CG.kCGHIDEventTap, mouse_up)
