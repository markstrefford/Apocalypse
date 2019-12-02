# Deep Photo Transfer for VFX

This code aims to improve on the work of Fujun Luan, Sylvain Paris, Eli Shechtman and Kavita Bala in their paper "Deep Phot Style Transfer" (https://arxiv.org/abs/1703.07511). The code works well on the provided examples, but I have identified issues transering style between somewhat dissimilar images.

For example, with the following images:

* Content image

![Content image](readme_images/new_buildings_1.jpeg)

* Content mask

![Content mask](readme_images/new_buildings_mask.png)

* Style image

![Style image](readme_images/future_style.jpg)

* Style mask

![Future style mask](readme_images/future_style_mask_0.png)

The following output is generated:

* Epoch 550

![Epoch 550 output](readme_images/temp_result_550.png)

* Epoch 3000

![Epoch 3000 output](readme_images/temp_result_3000.png)

* Final / best output

![Final output](readme_images/temp_result_deep_style_tranfer.png)

As can be seen in this final output, much of the unmasked area of the image has been in-painted, 
and the style is more reflective of painting than photo transfer. 
This is not evident in other photos, and suggests the following may not hold true in the current algorithm:

1) The masks are used accurately in calculating loss
1) Back propagation is ignoring the masks when adjusting the source image
1) The implementation of the code is bugged, and therefore the loss is not being calculated correctly (assume this is not true as in many examples the algorithm works)
1) The final step of the process performs some additional image manipulation which could be improved
1) The particular style image is too complex and doesn't translate well to the source image domain
1) The hyperparameters used for loss, etc. need modifying
1) The configuration of VGG19, including loss metrics at various layers, needs re-working for a wider set of use cases

