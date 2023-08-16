import numpy as np

K = 1
G = 0.7
ndim = 2
kronecker = np.eye(ndim)


def get_s(a: np.ndarray) -> np.ndarray:
    return a - np.trace(a) / ndim * kronecker


def stress_cal(eps: np.ndarray) -> np.ndarray:
    e = get_s(eps)
    eps_v = np.trace(eps)
    return eps_v * K * kronecker + e * 2 * G


def cal_theta(s: np.ndarray) -> float:
    # 计算矩阵的特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(s)

    # 找到最大特征值的索引
    max_eigenvalue_index = np.argmax(eigenvalues)

    # 对应的特征向量即为主轴方向
    main_axis = eigenvectors[:, max_eigenvalue_index]

    # 计算主轴方向与x轴之间的夹角（偏转角）
    angle_radians = np.arctan2(main_axis[1], main_axis[0])

    # 将弧度转换为度数
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees


def cal_print(s: np.ndarray):
    strain_temp = s
    stress_temp = stress_cal(strain_temp)
    angle_sig, angle_eps = cal_theta(s=strain_temp), cal_theta(stress_temp)

    print("\n" + "="*20)
    print("The strain is \n", strain_temp, "\nthe stress is \n", stress_temp)
    print("The angle of strain is %f" % angle_sig)
    print("The angle of stress is %f" % angle_eps)


if __name__ == "__main__":
    cal_print(np.diag([1, 2]))
    cal_print(np.array([[1, 2], [3, 4]]))
