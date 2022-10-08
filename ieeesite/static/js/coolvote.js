const littles = document.querySelectorAll(".little span");

littles.forEach((little, i) => {
  little.animate(
    [
      {
        transform: "translateX(100%)",
        opacity: 0,
        easing: "cubic-bezier(.5,-0.15,.49,1.25)"
      },
      {
        transform: "translateX(0%)",
        opacity: 1,
        offset: 0.15,
        easing: "cubic-bezier(.5,-0.155,.49,1.25)"
      },
      {
        transform: "translateX(0%)",
        opacity: 1,
        offset: 0.8,
        easing: "cubic-bezier(.5,-0.155,.49,1.25)"
      },
      {
        transform: "translateX(-100%)",
        opacity: 0,
        easing: "cubic-bezier(.5,-0.155,.49,1.25)"
      }
    ],
    {
      duration: 10000,
      delay: -5000 * i,
      iterations: Infinity,
      easing: "cubic-bezier(.5,-0,.49,1.25)"
    }
  );
});
