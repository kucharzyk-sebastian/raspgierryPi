class Text:
    @staticmethod
    def render_centered_text(surface, center_x, center_y, font, text, color, antialias=False):
        text_surface_obj = font.render(text, antialias, color)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (center_x, center_y)
        surface.blit(text_surface_obj, text_rect_obj)
