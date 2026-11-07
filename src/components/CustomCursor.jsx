import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';

export default function CustomCursor() {
  const [mousePosition, setMousePosition] = useState({ x: -100, y: -100 });
  const [isHoveringInteractive, setIsHoveringInteractive] = useState(false);
  const [isTouchDevice, setIsTouchDevice] = useState(false);

  useEffect(() => {
    if (window.matchMedia('(pointer: coarse)').matches) {
      setIsTouchDevice(true);
      return;
    }

    const updateMousePosition = (e) => {
      setMousePosition({ x: e.clientX, y: e.clientY });
    };

    const handleMouseOver = (e) => {
      const target = e.target;
      if (
        target.tagName === 'A' ||
        target.tagName === 'BUTTON' ||
        target.closest('a') ||
        target.closest('button') ||
        target.tagName === 'INPUT' ||
        target.tagName === 'TEXTAREA'
      ) {
        setIsHoveringInteractive(true);
      } else {
        setIsHoveringInteractive(false);
      }
    };

    window.addEventListener('mousemove', updateMousePosition, { passive: true });
    window.addEventListener('mouseover', handleMouseOver, { passive: true });

    return () => {
      window.removeEventListener('mousemove', updateMousePosition);
      window.removeEventListener('mouseover', handleMouseOver);
    };
  }, []);

  if (isTouchDevice) return null;

  return (
    <>
      <div
        className="pointer-events-none fixed inset-0 z-30 transition-opacity duration-300 hidden lg:block"
        style={{
          background: `radial-gradient(500px circle at ${mousePosition.x}px ${mousePosition.y}px, rgba(59, 130, 246, 0.07), transparent 70%)`,
        }}
      />

      <motion.div
        className="pointer-events-none fixed top-0 left-0 z-50 hidden lg:block rounded-full border border-blue-400/50 mix-blend-screen"
        animate={{
          x: mousePosition.x - (isHoveringInteractive ? 24 : 16),
          y: mousePosition.y - (isHoveringInteractive ? 24 : 16),
          width: isHoveringInteractive ? 48 : 32,
          height: isHoveringInteractive ? 48 : 32,
          backgroundColor: isHoveringInteractive
            ? 'rgba(139, 92, 246, 0.15)'
            : 'rgba(59, 130, 246, 0.03)',
        }}
        transition={{ type: 'spring', stiffness: 350, damping: 28, mass: 0.4 }}
      />
    </>
  );
}
