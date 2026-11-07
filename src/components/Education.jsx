import React, { useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { GraduationCap, MapPin, Award, CheckCircle } from 'lucide-react';
import { educationData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

gsap.registerPlugin(ScrollTrigger);

export default function Education() {
  const timelineRef = useRef(null);
  const progressLineRef = useRef(null);

  useEffect(() => {
    const ctx = gsap.context(() => {
      if (progressLineRef.current && timelineRef.current) {
        gsap.fromTo(
          progressLineRef.current,
          { scaleY: 0 },
          {
            scaleY: 1,
            ease: 'none',
            scrollTrigger: {
              trigger: timelineRef.current,
              start: 'top 75%',
              end: 'bottom 65%',
              scrub: 0.6,
            },
          }
        );
      }
    }, timelineRef);

    return () => ctx.revert();
  }, []);

  return (
    <section id="education" className="py-20 sm:py-28 relative">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="04. ACADEMIC JOURNEY"
          title="Education &"
          highlight="Qualifications"
          subtitle="A strong computer science foundation highlighted by an 8.76 CGPA in B.Tech CSE."
        />

        <div ref={timelineRef} className="relative pl-6 sm:pl-10">
          <div className="absolute left-2.5 sm:left-4 top-2 bottom-2 w-1 rounded-full bg-slate-200 dark:bg-white/10" />

          <div
            ref={progressLineRef}
            className="absolute left-2.5 sm:left-4 top-2 bottom-2 w-1 rounded-full bg-gradient-to-b from-blue-500 via-purple-500 to-cyan-400 origin-top"
          />

          <div className="space-y-10">
            {educationData.map((item, idx) => (
              <motion.div
                key={item.id}
                initial={{ opacity: 0, x: 25 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true, amount: 0.25 }}
                transition={{ duration: 0.5, delay: idx * 0.1 }}
                className="relative"
              >
                <div className="absolute -left-[1.65rem] sm:-left-[2.15rem] top-6 w-5 h-5 rounded-full bg-[#050816] border-4 border-blue-500 shadow-lg shadow-blue-500/50" />

                <TiltCard className="glass-card rounded-3xl p-6 sm:p-8">
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 mb-4 border-b border-slate-200/80 dark:border-white/10">
                    <div className="flex items-start gap-3.5">
                      <div className="p-3 rounded-2xl bg-gradient-to-br from-blue-600 to-purple-600 text-white shadow-md shrink-0">
                        <GraduationCap className="w-6 h-6" />
                      </div>
                      <div>
                        <span className="text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 font-semibold">
                          {item.period}
                        </span>
                        <h3 className="font-display text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
                          {item.degree}
                        </h3>
                        <p className="text-sm font-medium text-slate-700 dark:text-slate-300 mt-0.5">
                          {item.institution}
                        </p>
                      </div>
                    </div>

                    <div className="flex sm:flex-col items-start sm:items-end gap-2 shrink-0">
                      <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-600 dark:text-emerald-400 font-mono text-xs font-bold">
                        <Award className="w-4 h-4" />
                        {item.scoreLabel}: {item.score}
                      </span>
                      <span className="inline-flex items-center gap-1 text-xs text-slate-500 dark:text-slate-400">
                        <MapPin className="w-3.5 h-3.5 text-blue-400" />
                        {item.location}
                      </span>
                    </div>
                  </div>

                  <ul className="space-y-2.5">
                    {item.highlights.map((point, i) => (
                      <li
                        key={i}
                        className="flex items-start gap-2.5 text-sm text-slate-600 dark:text-slate-300"
                      >
                        <CheckCircle className="w-4 h-4 text-blue-500 shrink-0 mt-0.5" />
                        <span>{point}</span>
                      </li>
                    ))}
                  </ul>
                </TiltCard>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
