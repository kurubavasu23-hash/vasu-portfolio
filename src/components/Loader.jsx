import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Terminal, Code2 } from 'lucide-react';

export default function Loader({ onComplete }) {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 100) {
          clearInterval(interval);
          setTimeout(onComplete, 250);
          return 100;
        }
        return prev + 5;
      });
    }, 30);

    return () => clearInterval(interval);
  }, [onComplete]);

  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 1 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.5, ease: 'easeInOut' }}
        className="fixed inset-0 z-[100] flex flex-col items-center justify-center bg-[#050816] text-white px-6"
      >
        <div className="absolute w-96 h-96 rounded-full bg-blue-600/20 blur-[120px] pointer-events-none" />
        <div className="absolute w-80 h-80 rounded-full bg-purple-600/20 blur-[120px] pointer-events-none" />

        <motion.div
          initial={{ scale: 0.85, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.4 }}
          className="relative flex flex-col items-center max-w-md w-full"
        >
          <div className="relative mb-6 flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-blue-500/20 via-indigo-500/20 to-purple-500/20 border border-white/15 shadow-2xl shadow-blue-500/20">
            <span className="font-display text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-purple-400 to-cyan-400">
              KV
            </span>
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ duration: 8, repeat: Infinity, ease: 'linear' }}
              className="absolute -inset-1.5 rounded-2xl border border-dashed border-blue-400/40"
            />
          </div>

          <h1 className="font-display text-xl sm:text-2xl font-bold tracking-tight text-white mb-1">
            Kuruba Vasu
          </h1>
          <p className="font-mono text-xs sm:text-sm text-blue-400 mb-6 flex items-center gap-1.5">
            <Terminal className="w-3.5 h-3.5" />
            <span>Initializing Full Stack Portfolio Environment...</span>
          </p>

          <div className="w-full h-2 bg-white/10 rounded-full overflow-hidden mb-3 p-0.5">
            <motion.div
              className="h-full rounded-full bg-gradient-to-r from-blue-500 via-purple-500 to-cyan-400"
              style={{ width: `${progress}%` }}
            />
          </div>

          <div className="w-full flex justify-between items-center font-mono text-xs text-slate-400">
            <span className="flex items-center gap-1">
              <Code2 className="w-3.5 h-3.5 text-purple-400" />
              Python • Django • React.js
            </span>
            <span className="text-cyan-400 font-semibold">{progress}%</span>
          </div>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
}
