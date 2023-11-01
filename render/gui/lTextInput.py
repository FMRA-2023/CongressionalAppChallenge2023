import pygame

from render.gui.base.font import RobotoSlab
from render.gui.base.renderable import Renderable
from render.gui.base.text import Text
from render.gui.elements.textinput import TextInput


class LongTextInput(TextInput):
    def __init__(self, x, y, maxWidth, maxLen=None):
        super().__init__(x, y, Text("", RobotoSlab.retrieve("light", 12), (0, 0, 0), (x, y)), maxLen=maxLen)
        self.maxWidth = maxWidth
        self.renderText = None
    
    def tick(self, dt, mousePos, mouseClicked, prevClicked, keys, prevKeys):
        super().tick(dt, mousePos, mouseClicked, prevClicked, keys, prevKeys)
        keyP = lambda x: self.keyPressed(x, keys, prevKeys)
        if keyP(pygame.K_RETURN):
            self.insertAtCursor("\n")
            self.cursor+=1
            self.cursorDelay = 0
            self.cursorFlash = True

        renderText = self.text
        if self.subchar != "":
            renderText = self.subchar * (len(self.text))

        spacedText = ""
        spaceOffsets = []
        offset = 0
        for word in renderText.split(" "):
            newLine = "\n"
            if Text(f"{spacedText.split(newLine)[-1]} {word}", self.textObj.font, (0, 0, 0), self.textObj.pos).w > self.maxWidth:
                wordSplit = ""
                for char in word:
                    if Text(f"{wordSplit}{char}", self.textObj.font, (0, 0, 0), self.textObj.pos).w > self.maxWidth:
                        wordSplit = f"{wordSplit}\n{char}"
                        spaceOffsets.append(offset)
                        offset += 1


                    else:
                        wordSplit = f"{wordSplit}{char}"
                spacedText = f"{spacedText}\n{wordSplit}"
                spaceOffsets.append(offset)


            else:
                if "\n" in word:
                    spaceOffsets.append(offset)
                spacedText = f"{spacedText} {word}"

        renderText = spacedText.lstrip()
        self.renderText = renderText
        self.textObj.set_text(renderText)

        lines = renderText[:self.cursor].count("\n")+1
        renderCursor = self.cursor + (spaceOffsets[lines - 2] if lines > 1 else 0)
        thisLineText = renderText[:renderCursor].split("\n")[-1]

        whereCursor = self.textObj.pos[0] + Text(thisLineText, self.textObj.font, (0, 0, 0), self.textObj.pos).w
        whereCursorY = self.textObj.pos[1] + Text(renderText[:renderCursor], self.textObj.font, (0, 0, 0), self.textObj.pos).h
        renderObjs = [Renderable(pygame.Rect(self.x, self.y, self.textObj.w + 10, self.textObj.h + 5), (195, 215, 255) if self.active else (255, 255, 255), 0),
                      Renderable(self.textObj)]
        if self.active:
            if self.cursorFlash:
                renderObjs.append(Renderable(pygame.Rect(whereCursor, whereCursorY-1-Text("h", self.textObj.font, (0, 0, 0), (0, 0)).h, 2, Text("h", self.textObj.font, (0, 0, 0), (0, 0)).h-1), (0, 0, 0), 0))
        self.renderables = renderObjs
        self.recalculateWH()
