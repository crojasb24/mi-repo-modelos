def mostrar_imagen(img_bgr, titulo='Imagen'):
    """Muestra una imagen BGR (OpenCV) convertida a RGB."""
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(5,5))
    plt.imshow(img_rgb)
    plt.title(titulo)
    plt.axis('off')
    plt.show()