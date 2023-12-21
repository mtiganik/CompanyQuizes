import React from "react";

function ImageGallery({ images }) {
    // Use browser console and console.log() for debugging
    const arrayChunk = (arr, n) => {
        const array = arr.slice();
        const chunks = [];
        while (array.length) chunks.push(array.splice(0, n));
        return chunks;
      };
      
    return <div>
        {arrayChunk(images, 3).map((row,i) =>(
            <div key={i} className="row mx-auto">
                {row.map((col, i) =>(
                    <LazyImg key={i} src={col} height="200px" width="200px" loading="lazy"/>
                ))}
                </div>
        ))}
    </div>;
}

const LazyImg = props => {
    const [inView, setInView] = React.useState(false);
    const placeholderRef = React.useRef();
    const placeholder = ""


    React.useEffect(() => {
        const observer = new IntersectionObserver((entries, obs) => {
        for (const entry of entries) {
            if (entry.isIntersecting) {
                setInView(true);
                obs.disconnect();
            }
        }
   }, {});
    observer.observe(placeholderRef.current);
    return () => {
        observer.disconnect();
    }
}, []);
return (
    inView ? <img {...props} alt={props.alt || ""} /> : <img {...props} ref={placeholderRef} src={placeholder} alt={props.alt || ""} />
)
};


export default ImageGallery;



