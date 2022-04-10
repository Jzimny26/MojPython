class ItemBase:
    def __init__(self, Name, Weight: float, Description):
        self.Name = Name
        self.Weight = Weight
        self.LevelLimitation = 0
        self.ClassLimitation = []
        self.Description = Description