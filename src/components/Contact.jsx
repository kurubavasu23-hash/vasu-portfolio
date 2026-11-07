import React, { useState } from 'react';
import { motion } from 'framer-motion';
import {
  Mail,
  MapPin,
  Github,
  Linkedin,
  Send,
  CheckCircle2,
  AlertCircle,
  Copy,
  Check,
} from 'lucide-react';
import { personalInfo } from '../data/portfolioData';
import SectionHeading from './SectionHeading';

export default function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });
  const [status, setStatus] = useState({ type: '', message: '' });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [copiedEmail, setCopiedEmail] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const copyEmailToClipboard = () => {
    navigator.clipboard.writeText(personalInfo.email);
    setCopiedEmail(true);
    setTimeout(() => setCopiedEmail(false), 2500);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus({ type: '', message: '' });

    if (
      !formData.name.trim() ||
      !formData.email.trim() ||
      !formData.subject.trim() ||
      !formData.message.trim()
    ) {
      setStatus({
        type: 'error',
        message: 'Please fill out all fields before sending your message.',
      });
      return;
    }

    setIsSubmitting(true);

    const web3FormsKey = import.meta.env.VITE_WEB3FORMS_ACCESS_KEY;
    const formspreeEndpoint = import.meta.env.VITE_FORMSPREE_ENDPOINT;

    try {
      if (web3FormsKey) {
        const res = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({
            access_key: web3FormsKey,
            name: formData.name,
            email: formData.email,
            subject: formData.subject,
            message: formData.message,
          }),
        });
        const data = await res.json();
        if (data.success) {
          setStatus({
            type: 'success',
            message: 'Thank you! Your message has been sent directly to Kuruba Vasu.',
          });
          setFormData({ name: '', email: '', subject: '', message: '' });
          setIsSubmitting(false);
          return;
        }
      } else if (formspreeEndpoint) {
        const res = await fetch(formspreeEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(formData),
        });
        if (res.ok) {
          setStatus({
            type: 'success',
            message: 'Thank you! Your message has been delivered successfully.',
          });
          setFormData({ name: '', email: '', subject: '', message: '' });
          setIsSubmitting(false);
          return;
        }
      }

      const mailtoSubject = encodeURIComponent(
        `[Portfolio Inquiry] ${formData.subject} — from ${formData.name}`
      );
      const mailtoBody = encodeURIComponent(
        `Name: ${formData.name}\nEmail: ${formData.email}\nSubject: ${formData.subject}\n\nMessage:\n${formData.message}`
      );
      window.location.href = `mailto:${personalInfo.email}?subject=${mailtoSubject}&body=${mailtoBody}`;

      setStatus({
        type: 'success',
        message:
          'Your email client has been opened with your pre-filled message to Kuruba Vasu!',
      });
      setFormData({ name: '', email: '', subject: '', message: '' });
    } catch {
      setStatus({
        type: 'error',
        message:
          'Something went wrong while sending. Please use the direct email link alongside this form.',
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <section id="contact" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="07. GET IN TOUCH"
          title="Let's Build Something"
          highlight="Impactful Together"
          subtitle="Hiring for a Python Full Stack Developer or Software Engineer role? Send a message or connect directly via LinkedIn, GitHub, or Email."
        />

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <motion.div
            initial={{ opacity: 0, x: -24 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.25 }}
            transition={{ duration: 0.5 }}
            className="lg:col-span-5 space-y-5"
          >
            <div className="glass-card rounded-3xl p-7">
              <h3 className="font-display text-2xl font-bold text-slate-900 dark:text-white mb-2">
                Contact Information
              </h3>
              <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-6">
                I am actively seeking full-time Software Developer and Python Full Stack Developer opportunities. Feel free to reach out!
              </p>

              <div className="space-y-4">
                <div className="p-4 rounded-2xl glass-pill flex items-center justify-between gap-3">
                  <div className="flex items-center gap-3.5 min-w-0">
                    <div className="p-3 rounded-xl bg-blue-500/15 text-blue-500 shrink-0">
                      <Mail className="w-5 h-5" />
                    </div>
                    <div className="min-w-0">
                      <div className="text-xs font-mono text-slate-400">
                        Email Address
                      </div>
                      <a
                        href={personalInfo.socials.email}
                        className="text-sm font-semibold text-slate-900 dark:text-white hover:text-blue-500 truncate block"
                      >
                        {personalInfo.email}
                      </a>
                    </div>
                  </div>
                  <button
                    onClick={copyEmailToClipboard}
                    title="Copy Email Address"
                    className="p-2 rounded-lg glass-pill text-slate-500 hover:text-blue-500 shrink-0"
                  >
                    {copiedEmail ? (
                      <Check className="w-4 h-4 text-emerald-500" />
                    ) : (
                      <Copy className="w-4 h-4" />
                    )}
                  </button>
                </div>

                <div className="p-4 rounded-2xl glass-pill flex items-center gap-3.5">
                  <div className="p-3 rounded-xl bg-purple-500/15 text-purple-500 shrink-0">
                    <MapPin className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="text-xs font-mono text-slate-400">
                      Location
                    </div>
                    <div className="text-sm font-semibold text-slate-900 dark:text-white">
                      {personalInfo.location}
                    </div>
                  </div>
                </div>
              </div>

              <div className="mt-7 pt-6 border-t border-slate-200/80 dark:border-white/10">
                <div className="text-xs font-mono uppercase tracking-wider text-slate-400 mb-3">
                  Professional Profiles
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <a
                    href={personalInfo.socials.github}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center justify-center gap-2 py-3 px-4 rounded-xl glass-pill text-sm font-semibold text-slate-800 dark:text-white hover:bg-blue-600 hover:text-white dark:hover:bg-blue-600 transition-all"
                  >
                    <Github className="w-4 h-4" />
                    <span>GitHub</span>
                  </a>
                  <a
                    href={personalInfo.socials.linkedin}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center justify-center gap-2 py-3 px-4 rounded-xl glass-pill text-sm font-semibold text-slate-800 dark:text-white hover:bg-blue-600 hover:text-white dark:hover:bg-blue-600 transition-all"
                  >
                    <Linkedin className="w-4 h-4" />
                    <span>LinkedIn</span>
                  </a>
                </div>
              </div>
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 24 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.25 }}
            transition={{ duration: 0.5 }}
            className="lg:col-span-7 glass-card rounded-3xl p-7 sm:p-9"
          >
            <h3 className="font-display text-2xl font-bold text-slate-900 dark:text-white mb-6">
              Send Me a Message
            </h3>

            <form onSubmit={handleSubmit} className="space-y-5" noValidate>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                <div>
                  <label
                    htmlFor="name"
                    className="block text-xs font-mono uppercase tracking-wider text-slate-600 dark:text-slate-300 mb-2"
                  >
                    Your Name *
                  </label>
                  <input
                    id="name"
                    name="name"
                    type="text"
                    required
                    value={formData.name}
                    onChange={handleChange}
                    placeholder="Enter your name"
                    className="w-full px-4 py-3.5 rounded-xl bg-slate-100/80 dark:bg-white/[0.05] border border-slate-300 dark:border-white/10 text-slate-900 dark:text-white placeholder-slate-400 text-sm focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all"
                  />
                </div>

                <div>
                  <label
                    htmlFor="email"
                    className="block text-xs font-mono uppercase tracking-wider text-slate-600 dark:text-slate-300 mb-2"
                  >
                    Your Email *
                  </label>
                  <input
                    id="email"
                    name="email"
                    type="email"
                    required
                    value={formData.email}
                    onChange={handleChange}
                    placeholder="name@company.com"
                    className="w-full px-4 py-3.5 rounded-xl bg-slate-100/80 dark:bg-white/[0.05] border border-slate-300 dark:border-white/10 text-slate-900 dark:text-white placeholder-slate-400 text-sm focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all"
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="subject"
                  className="block text-xs font-mono uppercase tracking-wider text-slate-600 dark:text-slate-300 mb-2"
                >
                  Subject *
                </label>
                <input
                  id="subject"
                  name="subject"
                  type="text"
                  required
                  value={formData.subject}
                  onChange={handleChange}
                  placeholder="Software Developer Role / Project Opportunity"
                  className="w-full px-4 py-3.5 rounded-xl bg-slate-100/80 dark:bg-white/[0.05] border border-slate-300 dark:border-white/10 text-slate-900 dark:text-white placeholder-slate-400 text-sm focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all"
                />
              </div>

              <div>
                <label
                  htmlFor="message"
                  className="block text-xs font-mono uppercase tracking-wider text-slate-600 dark:text-slate-300 mb-2"
                >
                  Message *
                </label>
                <textarea
                  id="message"
                  name="message"
                  rows="5"
                  required
                  value={formData.message}
                  onChange={handleChange}
                  placeholder="Hello Vasu, we came across your portfolio and would love to discuss..."
                  className="w-full px-4 py-3.5 rounded-xl bg-slate-100/80 dark:bg-white/[0.05] border border-slate-300 dark:border-white/10 text-slate-900 dark:text-white placeholder-slate-400 text-sm focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all resize-none"
                />
              </div>

              {status.message && (
                <div
                  className={`p-4 rounded-xl flex items-start gap-3 text-sm ${
                    status.type === 'success'
                      ? 'bg-emerald-500/10 border border-emerald-500/30 text-emerald-600 dark:text-emerald-300'
                      : 'bg-rose-500/10 border border-rose-500/30 text-rose-600 dark:text-rose-300'
                  }`}
                >
                  {status.type === 'success' ? (
                    <CheckCircle2 className="w-5 h-5 shrink-0 mt-0.5" />
                  ) : (
                    <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
                  )}
                  <span>{status.message}</span>
                </div>
              )}

              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full btn-primary py-4 text-sm sm:text-base disabled:opacity-60"
              >
                <Send className="w-4 h-4" />
                <span>{isSubmitting ? 'Sending Message...' : 'Send Message'}</span>
              </button>
            </form>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
