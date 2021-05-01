import pygame
import pathlib


class TextButton:

    def __init__(self, screen, x, y, w, h, text,
                 color_bg_active=(42, 157, 143),
                 color_bg_inactive=(0, 0, 0),
                 color_text=(255, 255, 255),
                 alpha=128,
                 text_alignment='CENTER',
                 sliding_disappearance=False,
                 resize_right=False):
        """
        Creates a button:
            - on activation sliding to the left or inplace
            - on activation fading optionally available
            - Active highlighting and resizing to the right (background width + font)
            - Text alignment options: `['LEFT', 'CENTER', 'RIGHT']`
            - Returns button text if clicked, else None
        """
        # Position
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sliding_disappearance = sliding_disappearance
        self.resize_right = resize_right
        self.fading_steps = 5  # decreasing steps of alpha on fading
        self.sliding_steps = 25  # sliding steps to the left
        self.alpha_border = 25  # if alpha falls below this value, the text is not being rendered anymore
        self.alpha = alpha
        self.color_bg_active = color_bg_active
        self.color_bg_inactive = color_bg_inactive
        self.text_alignment = text_alignment

        # Original values used for reset
        self.x_original = x
        self.alpha_original = alpha

        # Button "background" - active
        self.active_background_surface = pygame.Surface((w, h))
        self.active_background_surface.set_alpha(self.alpha)
        self.active_background_surface.fill(self.color_bg_active)
        # Button "background" - inactive
        self.inactive_background_surface = pygame.Surface((w, h))
        self.inactive_background_surface.set_alpha(self.alpha)
        self.inactive_background_surface.fill(self.color_bg_inactive)

        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text

        # Text - at the center of the button
        pygame.font.init()
        self.color_text = color_text

        self.active_font = pygame.font.Font("resources/Fonts/Quicksand-SemiBold.ttf", 20)
        self.active_text_surface = None
        self.active_textRect = None
        # inactive
        self.inactive_font = pygame.font.Font("resources/Fonts/Quicksand-Bold.ttf", 22)
        self.inactive_text_surface = None
        self.inactive_textRect = None
        self.reset()

    def reset(self):
        """
        Rebuilds the surfaces based on the original positions and alpha value.

        This can be used to reset the states of buttons after returning to a Menu a second time.
        """
        self.x = self.x_original
        self.alpha = self.alpha_original

        # Button "background" - active
        self.active_background_surface.set_alpha(self.alpha)
        # Button "background" - inactive
        self.inactive_background_surface.set_alpha(self.alpha)

        # active
        self.active_text_surface = self.active_font.render(self.text, True, self.color_text)
        self.active_textRect = self.active_text_surface.get_rect()
        # inactive
        self.inactive_text_surface = self.inactive_font.render(self.text, True, self.color_text)
        self.inactive_textRect = self.inactive_text_surface.get_rect()

        if self.text_alignment == 'CENTER':
            self.active_textRect.center = ((self.x + (self.rect.w / 2)), (self.y + (self.rect.h / 2)))
            self.inactive_textRect.center = ((self.x + (self.rect.w / 2)), (self.y + (self.rect.h / 2)))

        elif self.text_alignment == 'RIGHT':
            self.active_textRect.centery = self.y + (self.rect.h / 2)
            self.active_textRect.right = self.x + self.w - 15  # padding of 15
            self.inactive_textRect.centery = self.y + (self.rect.h / 2)
            self.inactive_textRect.right = self.x + self.w - 15  # padding of 15

        else:  # LEFT (or invalid)
            self.active_textRect.centery = self.y + (self.rect.h / 2)
            self.active_textRect.left = self.x + 15  # padding of 15
            self.inactive_textRect.centery = self.y + (self.rect.h / 2)
            self.inactive_textRect.left = self.x + 15  # padding of 15

    def render(self, mouse, events, fading=False):
        """
        Checks which rendering is needed and renders the button onto the screen surface.
        Checks whether the button was clicked and if so, returns the text of the button.
        """

        clicked = True if pygame.MOUSEBUTTONDOWN in [e.type for e in events] else False
        if fading:
            self.render_fading()
        elif self.mouse_on_button(mouse):
            self.render_active()
            if clicked:  # mouse on button + click
                return self.text
        else:
            self.render_inactive()
            return None  # readability - return explicitly None if button was not clicked

    def render_inactive(self):
        """
        Rendering the inactive button onto the screen surface.
        """
        # Rendering button "background"
        self.screen.blit(self.inactive_background_surface, (self.x, self.y))
        # Rendering button text
        self.screen.blit(self.active_text_surface, self.active_textRect)

    def render_active(self):
        """
        Rendering the active button onto the screen surface.
        """
        # Rendering button "background"
        if self.resize_right:
            self.active_background_surface = pygame.Surface((self.w * 1.05, self.h))
        else:
            self.active_background_surface = pygame.Surface((self.w, self.h))
        self.active_background_surface.set_alpha(self.alpha)
        self.active_background_surface.fill(self.color_bg_active)
        self.screen.blit(self.active_background_surface, (self.x, self.y))  # (0,0) are the top-left coordinates
        # Rendering button text
        self.screen.blit(self.inactive_text_surface, self.inactive_textRect)

    def render_fading(self):
        """
        Renders the animation when a button was clicked
        """
        self.alpha = self.alpha - self.fading_steps
        self.inactive_background_surface.set_alpha(self.alpha)
        if self.sliding_disappearance:
            self.x -= self.sliding_steps
            self.active_textRect.x -= self.sliding_steps

        # Rendering button "background"
        self.screen.blit(self.inactive_background_surface, (self.x, self.y))  # (0,0) are the top-left coordinates
        if self.alpha > self.alpha_border:  # Render button text until its alpha value is reduced by x
            self.screen.blit(self.active_text_surface, self.active_textRect)

    def mouse_on_button(self, mouse) -> bool:
        """
        Checks whether the mouse is on the button and returns a boolean.
        """
        return self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y
