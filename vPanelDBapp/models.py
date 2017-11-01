from django.db import models

class HUGOgene(models.Model):
    ensemblGeneID = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.CharField(max_length=10)
    locationSortable = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol


class Panel(models.Model):
    Panel_Name = models.CharField(max_length=20, blank=True, null=True)
    Panel_ID = models.CharField(max_length=20, blank=True, null=True)
    Panel_Version = models.IntegerField(blank=True, null=True)
    Username = models.CharField(max_length=20, blank=True, null=True)
    HUGOgene = models.ManyToManyField(HUGOgene, blank=True)

    def __str__(self):
        return self.Panel_Name


class Subpanel(models.Model):
    Subpanel_Name = models.CharField(max_length=20, blank=True, null=True)
    Subpanel_ID = models.CharField(max_length=20, blank=True, null=True)
    Subpanel_Version = models.IntegerField(blank=True, null=True)
    Username = models.CharField(max_length=200, blank=True, null=True)
    HUGOgene = models.ForeignKey(HUGOgene, blank=True, null=True)
    Panel = models.ForeignKey(Panel, blank=True, null=True)


    def __str__(self):
        return self.Subpanel_Name