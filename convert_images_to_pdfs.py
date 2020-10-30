# GPL v3 or later
# author: Nic Freeman

import glob
import img2pdf
import os
import numpy as np
import sklearn.cluster
import distance
import fpdf
import PIL

# get the files
image_exts = ["jpg", "jpeg", "png"]
files = []
for ext in image_exts:
	files += glob.glob(os.path.join(".", "*."+ext))
	
# cluster the filenames 
words = np.array(files)
dists = -1*np.array([[distance.levenshtein(w1,w2) for w1 in files] for w2 in files])
affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5, random_state=0)
affprop.fit(dists)

# make one pdf output for each cluster of filenames
for cluster_id in np.unique(affprop.labels_):
	exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
	cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
	cluster_str = "\n".join(cluster)
	print(cluster_str, "\n")
	cluster.sort()
	
	pdf = fpdf.FPDF(unit="mm", format=[210,297]) # A4
	for image in cluster:
		pdf.add_page()
		pdf.image(image,0,0,210,297)
	pdf.output(cluster[0] + ".pdf", "F")

# delete the image files
for file in files:
	os.remove(file)