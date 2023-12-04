# import matplotlib.pyplot as plt
# import numpy as np

# # Ma'lumotlarni kiritish
# x_soat = np.array([1.0, 2.0, 3.0])
# y_baho = np.array([2.0, 4.0, 6.0])

# # To'g'ri hisoblash uchun funksiya


# def forward(x, w):
#     return x * w

# # Xatolik (Loss) ning funksiyasi


# def loss(x, y, w):
#     y_pred = forward(x, w)
#     return (y_pred - y) ** 2


# # Grafikni yaratib olishimiz uchun kontaynerlar
# w_list = []
# mse_list = []

# # w ni 0 dan 4 gacha oralig'ida hisblash
# for w in np.arange(0.0, 4.1, 0.1):
#     L_umum = 0

#     for x_hb_qiym, y_hb_qiym in zip(x_soat, y_baho):
#         L_hb_qiym = loss(x_hb_qiym, y_hb_qiym, w)
#         L_umum += L_hb_qiym

#     # Har bir ma'lumot uchun MSE ni hisoblaymiz
#     w_list.append(w)
#     mse_list.append(L_umum / len(x_soat))

# # Grafik natija
# plt.plot(w_list, mse_list)
# plt.ylabel('Loss')
# plt.xlabel('w')
# plt.gca().set_facecolor('#030101')  # Setting face color for the plot area
# plt.show()

# =============================================================================

# Kerakli kutubxonalrni chaqirib olish
# import torch

# x_soat = [1.0, 2.0, 3.0]
# y_baho = [2.0, 4.0, 6.0]

# w = torch.tensor([1.0], requires_grad=True)  # Taxminiy qiymat

# # (Modelimiz)To'g'ri hisoblash uchun funksiya


# def forward(x):
#     return x * w


# # Xatolik (Loss) ning funkisyasi
# def loss(y_pred, y_val):
#     return (y_pred - y_val) ** 2


# # Training dan avval
# print("Bashorat (training dan avval)",  "4 soat o'qilganda:", forward(4))

# # Training zanjiri (loop)
# learning_rate = 0.01
# for epoch in range(10):
#     for x_hb_qiym, y_hb_qiym in zip(x_soat, y_baho):
#         y_pred = forward(x_hb_qiym)  # 1) Forward hisoblash
#         l = loss(y_pred, y_hb_qiym)  # 2) Loss ni hisoblash
#         l.backward()  # 3) backward hisoblash
#         print("\tgrad: ", x_hb_qiym, y_hb_qiym, '{:.3f}'.format(w.grad.item()))
#         w.data = w.data - learning_rate * w.grad.item()  # W ning qiymatini yangilash

#         # w ning qiymattini yangilagach, nolga tenglashtirish
#         w.grad.data.zero_()

#     print(f"Epoch: {epoch} | Loss: {l.item()}")

# # Traningdan so'ng
# print("Bashorat (training dan keyin)",  "4 saot o'qilganda: ", forward(4))


# =================================================================================
# Kerakli kutubxonalarni chaqirib olish
import torch
import numpy as np
# Ma'lumotlarni tensor ko'rinishida yuklab olish
x_soat = torch.Tensor([[1.0],
                       [2.0],
                       [3.0]])
y_baho = torch.Tensor([[2.0],
                       [4.0],
                       [6.0]])

# (1) Class yordamida model qurib olish --> "Model"


class Model(torch.nn.Module):
    def __init__(self):
        # Bu yerda torch.nn.Module bu yerda super class(Pytorch)
        super().__init__()
        # torch.nn.Linear(#kirish, #chiqish) chiziqli model
        self.linear = torch.nn.Linear(1, 1)  # 1ta kirish & 1ta chiqish
    # Metod yordamida to'g'ri hisoblash funksiyasini kiritamiz(forward pass)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred


# Bizning model
model = Model()
# print(model)
# (2) Loss va optimizer larni tanlab olish
criterion = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
# (3) Training(3.1),   Backward(3.2), Step(3.3)
# (3.1)-->Training
for epoch in range(500):  # Epochlar soni 500
    y_pred = model(x_soat)
    # Loss|||xatolikni hisoblash va chop qilish
    loss = criterion(y_pred, y_baho)
    print(f'Epoch: {epoch} | Loss: {loss.item()} ')

    optimizer.zero_grad()  # Har bir epoch uchun grad ni 0 ga tenglashtirib olish
    # (3.2)-->Backpropagation|||Teskari hisoblash
    loss.backward()
    # (3.3)--> Step||| w ning qiymatini  yangilash
    optimizer.step()
# Bashorat uchun qiymat||| Ushbu qiymatimiz ham tensor bo'lishi kerak
soat_test = torch.Tensor([[4.]])
print("Bashorat (training dan keyin),  4 saot o'qilganda:",
      model.forward(soat_test).data[0][0].item())
