class SvgLinkEffect {
    constructor(effect) {
      if (effect.config.random) {
        this.randomizeArray(effect.nodes);
      }
  
      effect.element.addEventListener("click", () => {
        const reverse = effect.element.classList.contains("active");
        effect.element.classList.toggle("active");
        effect.handler(effect.nodes, effect.config, reverse);
      });
    }
  
    randomizeArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    }
  }
  
  const svgBounceEffect = (nodes, config, reverse) => {
    nodes.forEach((node, index) => {
      const { duration, ease, y1, y2, offset } = config;
      setTimeout(() => {
        const yValue = reverse ? y1 : y2;
        gsap.to(node, {
          duration: duration,
          ease: ease,
          y: yValue
        });
      }, index * offset);
    });
  };
  
  const svgAlternatingEffect = (nodes, config, reverse) => {
    nodes.forEach((node, index) => {
      const { duration, ease, offset } = config;
      setTimeout(() => {
        const yValue = reverse
          ? (index % 2 === 0 ? -44 : 44)
          : (index % 2 === 0 ? 44 : -44);
        gsap.to(node, {
          duration: duration,
          ease: ease,
          y: yValue
        });
      }, index * offset);
    });
  };
  
  document.addEventListener("DOMContentLoaded", () => {
    const cascadeLink = document.getElementById("cascade-link");
    if (cascadeLink) {
      const cascadeLinkEffect = {
        element: cascadeLink,
        handler: svgBounceEffect,
        nodes: [...cascadeLink.querySelectorAll("rect")],
        config: {
          offset: 10,
          duration: 1,
          random: true,
          ease: "expo.out",
          y1: -20,
          y2: 44
        }
      };
  
      new SvgLinkEffect(cascadeLinkEffect);
    }
  });
  