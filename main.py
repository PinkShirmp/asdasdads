from manim import *
from manim_slides import Slide
import numpy as np



class Introduction(Slide,MovingCameraScene,Scene):
    def SinxAndCosXVisualize(self):
        self.acc_time = 0
        def sceneUpdater(dt):
            self.acc_time += dt
        self.add_updater(sceneUpdater)

        outputScope2 = VGroup()
        plta = FunctionGraph( lambda x: 0, x_range=[-2,2], color=YELLOW )
        pltb = FunctionGraph( lambda x: 0, x_range=[-2,2], color=BLUE )
        def outputdater2(mobj):            
            plta.become(FunctionGraph( lambda x: +0.20*np.sin(5*(x + self.acc_time)), x_range=[-2,2], color=YELLOW ).move_to(mobj))
            pltb.become(FunctionGraph( lambda x: -1.5*np.sin(5*(x + self.acc_time)), x_range=[-2,2], color=BLUE ).move_to(mobj))
        outputScope2.add_updater(outputdater2)
        rect = Rectangle(color=WHITE,height=4,width=4,grid_xstep=.8,grid_ystep=4/6, stroke_width=3)
        for mobj in rect[1]:
            mobj.set(stroke_width=1)
        for mobj in rect[2]:
            mobj.set(stroke_width=1)
        outputScope2.add(rect)
        outputScope2.add(plta,pltb)  
        self.update_self(self.acc_time)
        return outputScope2
    def construct(self):
        sinxcos=self.SinxAndCosXVisualize()
        self.add(sinxcos)
        nhom6=Text("NHÓM 6")
        nhom6.next_to(sinxcos[0],DOWN,0.25)
        self.play(Write(nhom6),run_time=1)
        for _ in range(1):  # You can adjust the number of loops here
            self.start_loop()
            self.wait()
            self.end_loop()
            self.clear()
            self.start_loop()

class Introduction2(Slide):
    def construct(self):
        Title=Text("Một bài thuyết trình ngắn gọn về",font_size=52,color=BLUE)
        Title.to_edge(ORIGIN)
        self.play(Write(Title),run_time=1)
        PhepViTu=Text("PHÉP VỊ TỰ",stroke_width=1,color=YELLOW)
        PhepViTu.next_to(Title,DOWN,buff=0.25)
        print(PhepViTu.get_center())
        PhepViTu.shift(np.array([5.0,0,0])) 
        self.play(Write(PhepViTu),run_time=0.5)
        self.next_slide()

        posforPHEPVITU=Text("mimi")
        posforPHEPVITU.to_edge(ORIGIN)
        posforPHEPVITU.to_edge(UP)

        self.play(PhepViTu.animate.move_to(posforPHEPVITU),FadeOut(Title),rate_functions=smooth)
        modau=Text("MỞ ĐẦU").match_style(PhepViTu)
        modau.to_edge(UP)
        self.play(ReplacementTransform(PhepViTu,modau))
        

class BaiToanMoDau(Slide):
    def construct(self):
        modau=Text("MỞ ĐẦU",stroke_width=1,color=YELLOW)
        modau.to_edge(UP)
        self.add(modau)
        sq01=Rectangle(width=2,height=4,fill_opacity=1,fill_color=BLUE)
        self.play(DrawBorderThenFill(sq01))
        self.next_slide()
        sq02=Rectangle(width=1,height=2,fill_opacity=1,fill_color=YELLOW)
        grp=VGroup(sq01,sq02)
        sq02.next_to(sq01,RIGHT,buff=0.25)
        self.play(Create(sq02),grp.animate.arrange(RIGHT,buff=2))
        self.next_slide()
        dot_B_sq1=self.createDot(1,UP,sq01,"$B'$",WHITE)
        dot_A_sq1=self.createDot(2,UP,sq01,"$A'$",WHITE)
        dot_D_sq1=self.createDot(3,DOWN,sq01,"$D'$",WHITE)
        dot_C_sq1=self.createDot(4,DOWN,sq01,"$C'$",WHITE)
        gr=VGroup(dot_A_sq1[0],dot_B_sq1[0],dot_C_sq1[0],dot_D_sq1[0])
        gr1=VGroup(dot_A_sq1[1],dot_B_sq1[1],dot_C_sq1[1],dot_D_sq1[1])

        dot_B_sq2=self.createDot(1,UP,sq02,"$B$",WHITE)
        dot_A_sq2=self.createDot(2,UP,sq02,"$A$",WHITE)
        dot_D_sq2=self.createDot(3,DOWN,sq02,"$D$",WHITE)
        dot_C_sq2=self.createDot(4,DOWN,sq02,"$C$",WHITE)
      
        gr_2=VGroup(dot_A_sq2[0],dot_B_sq2[0],dot_C_sq2[0],dot_D_sq2[0])
        gr1_2=VGroup(dot_A_sq2[1],dot_B_sq2[1],dot_C_sq2[1],dot_D_sq2[1])
        self.play(Create(dot_A_sq1[0]), Create(dot_B_sq1[0]), Create(dot_C_sq1[0]), Create(dot_D_sq1[0]))
        self.play(Create(dot_A_sq2[0]), Create(dot_B_sq2[0]), Create(dot_C_sq2[0]), Create(dot_D_sq2[0]))
        self.play(Write(gr1))
        self.play(Write(gr1_2))
        self.next_slide()
        DECAUA=Text(f"Giải thích vì sao các đường thẳng AA’, BB’, CC’, DD’ cùng đi qua một điểm O?",font_size=25)
        DECAUA.to_corner(DOWN)
        self.play(Write(DECAUA))
        smaler=VGroup(gr,gr1,gr_2,gr1_2,grp,DECAUA)
        self.next_slide()

        self.play(smaler.animate.scale(.5))
        self.play(smaler.animate.to_edge(LEFT))
        self.next_slide()
        
        chiachac=Line(UP,DOWN*2)
        self.play(Create(chiachac))


        intersection_point = self.calculateIntersection(dot_A_sq1[0].get_center(), dot_A_sq2[0].get_center(), dot_B_sq1[0].get_center(), dot_B_sq2[0].get_center())
        O=Dot(point=intersection_point)
        Otext=Tex("$O$")
        O.scale(.5)
        Otext.scale(.5)
        always_redraw(lambda:Otext.next_to(O,UP))
        self.play(Create(O),Write(Otext))
        AprimeOBprime=Polygon(dot_A_sq1[0].get_center(),O.get_center(),dot_B_sq1[0].get_center(),fill_opacity=0,color=WHITE)
        self.play(Create(AprimeOBprime))
        self.next_slide()
        #proofing
        #Xét tam giác OA'B' có AB // A'B'

        gr=VGroup(AprimeOBprime.copy(),dot_A_sq1[0].copy(),dot_A_sq1[1].copy(),dot_B_sq1[0].copy(),dot_B_sq1[1].copy(),dot_A_sq2[0].copy(),dot_A_sq2[1].copy(),dot_B_sq2[0].copy(),dot_B_sq2[1].copy(),O.copy(),Otext.copy())
        self.play(gr.animate.next_to(chiachac,RIGHT,buff=1))
        self.next_slide()
        l1=self.CreateLineBetweenPoints(gr[1],gr[3])
        l2=self.CreateLineBetweenPoints(gr[5],gr[7])

        g_l1l2=VGroup(l1,l2)
        self.play(g_l1l2.animate.set_color(RED),rate_functions=smooth)

        self.next_slide()
        self.play(FadeOut(gr),FadeOut(g_l1l2),run_time=1)
        thales = Tex(r"$$\frac{OA}{OA'}=\frac{OB}{OB'}=\frac{1}{2}$$", font_size=16)
        ketluan=Text(f"=> A,B lần lượt là trung điểm của A'O và B'O",font_size=16)
        
        loi_thoai=VGroup(Text("Xét tam giác OA'B',theo Thales, ta có:",font_size=16),thales,ketluan)
        loi_thoai.arrange(DOWN,0.25)

        loi_thoai.next_to(chiachac,RIGHT,0.25)
        self.play(Write(loi_thoai))
        self.play(loi_thoai.animate.move_to(loi_thoai.get_center() +UP))
        self.next_slide()
       # gr.next_to(loi_thoai,DOWN,buff=.5)
      #  self.play(Create(gr),run_time=1)

        
        


        
    def CreateLineBetweenPoints(self,From,To):
        l=Line(From,To)
        self.add(l)
        return l

    def calculateIntersection(self, point1, point2, point3, point4):
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        x3, y3 = point3[0], point3[1]
        x4, y4 = point4[0], point4[1]

        intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        return np.array([intersection_x, intersection_y, 0])


    def createDot(self,index,dir,sq,text,colorA,bufff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER):
        dot=always_redraw(lambda:Dot(sq.get_vertices()[index-1],color=colorA))
        texttt=Tex(text)
        always_redraw(lambda:texttt.next_to(dot,dir,buff=bufff))
        return [dot,texttt]


