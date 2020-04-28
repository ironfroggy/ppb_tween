import ppb
from ppb import keycodes
from ppb.events import KeyPressed, SceneStarted

import ppb_tween


class Player(ppb.BaseSprite):
    left = keycodes.Left
    right = keycodes.Right

    def on_scene_started(self, ev: SceneStarted, signal):
        self.position = ppb.Vector(-4, 0)
        self.tweener = ppb_tween.Tweener()
        ev.scene.add(self.tweener)

    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == self.left:
            self.tweener.tween(self, 'position', ppb.Vector(-4, 0), 1, easing='bounce_out')
        elif key_event.key == self.right:
            self.tweener.tween(self, 'position', ppb.Vector(4, 0), 1, easing='bounce_out')


def setup(scene):
    scene.add(Player())


ppb.run(setup, systems=(ppb_tween.Tweening,))
