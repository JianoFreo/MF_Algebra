from manim import *

class Test(Scene):
    def construct(self):
        eq = MathTex("E = mc^2")
        self.play(Write(eq))
        self.wait()