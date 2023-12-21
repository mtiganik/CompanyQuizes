import React, { useState, useRef, useEffect } from "react";

function ImageGallery({ images }) {
  const [visibleImages, setVisibleImages] = useState([]);
  const imageRefs = useRef([]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const index = imageRefs.current.indexOf(entry.target);
            if (index !== -1) {
              setVisibleImages((prevVisibleImages) => [
                ...prevVisibleImages,
                index
              ]);
              observer.unobserve(entry.target);
            }
          }
        });
      },
      { rootMargin: "100px 0px" }
    );
    imageRefs.current.forEach((imageRef) => observer.observe(imageRef));
    return () => {
      observer.disconnect();
    };
  }, [images]);

  return (
    <div style={{ display: "flex", flexWrap: "wrap" }}>
      {images.map((imageUrl, index) => (
        <img
          key={index}
          src={visibleImages.includes(index) ? imageUrl : ""}
          alt=""
          width={200}
          height={200}
          ref={(ref) => (imageRefs.current[index] = ref)}
          style={{ margin: "2px" }}
        />
      ))}
    </div>
  );
}

export default ImageGallery;
