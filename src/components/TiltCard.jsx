import React, { useState } from 'react';
import { motion } from 'framer-motion';

export default function TiltCard({ children, className = '' }) {
  const [rotateX, setRotateX] = useState(0);
  const [rotateY, setRotateY] = useState(0);
  const [glarePos, setGlarePos] = useState({ x: 50, y: 50 });
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const width = rect.width;
    const height = rect.height;
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    const rY = ((mouseX - width / 2) / width) * 10;
    const rX = -((mouseY - height / 2) / height) * 10;

    setRotateX(rX);
    setRotateY(rY);
    setGlarePos({
      x: (mouseX / width) * 100,
      y: (mouseY / height) * 100,
    });
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
    setRotateX(0);
    setRotateY(0);
  };

  return (
    <motion.div
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={handleMouseLeave}
      animate={{
        rotateX,
        rotateY,
        transformPerspective: 1100,
      }}
      transition={{ type: 'spring', stiffness: 260, damping: 22 }}
      style={{ transformStyle: 'preserve-3d' }}
      className={`relative overflow-hidden ${className}`}
    >
      {isHovered && (
        <div
          className="pointer-events-none absolute inset-0 z-10 transition-opacity duration-300"
          style={{
            background: `radial-gradient(320px circle at ${glarePos.x}% ${glarePos.y}%, rgba(59, 130, 246, 0.12), transparent 80%)`,
          }}
        />
      )}
      {children}
    </motion.div>
  );
}
