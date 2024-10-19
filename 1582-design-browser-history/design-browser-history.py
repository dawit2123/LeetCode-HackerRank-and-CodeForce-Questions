class BrowserHistory:

    def __init__(self, homepage: str):
        self.i=0
        self.length=1
        self.history=[homepage]

    def visit(self, url: str) -> None:
        if self.i+2>len(self.history):
            self.history.append(url)
        else:
            self.history[self.i+1]=url
        self.i+=1
        self.length=self.i+1

    def back(self, steps: int) -> str:
        self.i= max(self.i-steps, 0)
        return self.history[self.i]
    
    def forward(self, steps: int) -> str:
        self.i=min(self.i+steps, self.length-1)
        return self.history[self.i]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)