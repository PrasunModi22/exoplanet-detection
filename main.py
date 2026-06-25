from lightkurve import search_targetpixelfile
import matplotlib.pyplot as plt

pixelfile = search_targetpixelfile("KIC 8462852", quarter=16).download(quality_bitmask='hardest')

pixelfile.plot(frame=1)
plt.show()

lc = pixelfile.to_lightcurve(aperture_mask='all')
lc.plot()
plt.show()

pixelFile = search_targetpixelfile("KIC 6922244", quarter=4).download()
lc2 = pixelFile.to_lightcurve(aperture_mask=pixelFile.pipeline_mask)
lc2.plot()
plt.show()