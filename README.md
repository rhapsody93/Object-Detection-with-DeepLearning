[Build Custom Dataset]

① Object classes are set to six types: person, vehicle, truck, bus, bicycle, and motorcycle
② Select 50 images from the original dataset and enter them into Roboflow, proceed with auto-labeling
③ After auto-labeling is completed, all image data are inspected and objects that are not auto-labeled for each image are manually labeled
④ Complete image labeling and final inspection
⑤ train: validation: test = 6:2:2 data split and first learn from the YOLOv11 model within the tool
- train : 30 images
- validation : 10 images
- test : 10 images
⑥ Download custom dataset (image+annotation.txt) to prepare for direct model learning

![image](https://github.com/user-attachments/assets/d5a8f751-a732-48e8-a09a-785517309542)
![image](https://github.com/user-attachments/assets/4c811cd1-e652-4dbb-9469-aaa62942b4a0)
![image](https://github.com/user-attachments/assets/7947873c-88f1-474c-8c8c-25661dbe77e1)
![image](https://github.com/user-attachments/assets/8317e18b-ec74-4350-b384-5fc030c1996d)

[Training, Validation, Test with YOLOv8l.pt]

![image](https://github.com/user-attachments/assets/c301863f-d98e-4742-b9cd-d088d896d4d9)
![image](https://github.com/user-attachments/assets/4a564414-ea5c-4380-8641-bf5ca35d51a0)
![image](https://github.com/user-attachments/assets/aa379995-49f0-4dfa-83ed-0db9c337a724)
![image](https://github.com/user-attachments/assets/0856c4d7-396d-4390-b3ec-42715f52c422)
![image](https://github.com/user-attachments/assets/72a36104-2971-42fb-a9c0-b322986df77c)
![image](https://github.com/user-attachments/assets/6f4260fe-bf34-4fd2-9b50-dff340355d14)
![image](https://github.com/user-attachments/assets/6d88c4e0-707b-4bfb-88b5-e46fd5b22377)
