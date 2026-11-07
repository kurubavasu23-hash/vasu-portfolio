import os

FILES = {
    "package.json": r"""{
  "name": "kuruba-vasu-portfolio",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "description": "Personal Portfolio of Kuruba Vasu - Python Full Stack Developer & Software Developer",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "clsx": "^2.1.1",
    "framer-motion": "^11.2.10",
    "gsap": "^3.12.5",
    "lucide-react": "^0.395.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "tailwind-merge": "^2.3.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^4.3.1",
    "autoprefixer": "^10.4.19",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.4",
    "vite": "^5.3.1"
  }
}
""",

    "vite.config.js": r"""import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    open: true,
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
    minify: 'esbuild',
  },
});
""",

    "tailwind.config.js": r"""/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        display: ['Space Grotesk', 'Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      colors: {
        brand: {
          dark: '#050816',
          navy: '#0a0f24',
          card: '#0f1631',
          electric: '#3b82f6',
          cyan: '#06b6d4',
          purple: '#8b5cf6',
          pink: '#ec4899',
        },
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'hero-glow':
          'conic-gradient(from 180deg at 50% 50%, #3b82f633 0deg, #8b5cf633 180deg, #06b6d433 360deg)',
      },
      animation: {
        'pulse-slow': 'pulse 6s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
        'spin-slow': 'spin 14s linear infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-12px)' },
        },
      },
    },
  },
  plugins: [],
};
""",

    "postcss.config.js": r"""export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
""",

    "vercel.json": r"""{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ],
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
""",

    ".env.example": r"""# Optional: Add a Web3Forms Access Key (https://web3forms.com/) or Formspree endpoint
# to enable direct API form submissions without opening the user's email client.
VITE_WEB3FORMS_ACCESS_KEY=
VITE_FORMSPREE_ENDPOINT=
""",

    ".gitignore": r"""node_modules
dist
dist-ssr
*.local
.env
.env.*
!.env.example
.DS_Store
""",

    "index.html": r"""<!doctype html>
<html lang="en" class="dark scroll-smooth">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Kuruba Vasu | Python Full Stack Developer & Software Engineer</title>
    <meta
      name="description"
      content="Portfolio of Kuruba Vasu — Python Full Stack Developer, Software Developer, and B.Tech CSE Student at Dr. K.V. Subba Reddy Institute of Technology, Kurnool (CGPA 8.76). Skilled in Python, Django, React.js, JavaScript, REST APIs, and MySQL."
    />
    <meta
      name="keywords"
      content="Kuruba Vasu, Python Full Stack Developer, Software Developer, Django Developer, React Developer, B.Tech CSE, Kurnool, Dr. K.V. Subba Reddy Institute of Technology"
    />
    <meta name="author" content="Kuruba Vasu" />
    <meta property="og:title" content="Kuruba Vasu | Python Full Stack Developer" />
    <meta
      property="og:description"
      content="Explore the full-stack engineering projects, technical skills, and achievements of Kuruba Vasu."
    />
    <meta property="og:type" content="website" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap"
      rel="stylesheet"
    />
  </head>
  <body class="bg-[#050816] text-slate-100 antialiased selection:bg-blue-500 selection:text-white overflow-x-hidden">
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""",

    "public/favicon.svg": r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <rect width="100" height="100" rx="22" fill="#050816"/>
  <rect x="3" y="3" width="94" height="94" rx="19" stroke="url(#grad)" stroke-width="6"/>
  <path d="M26 30V70M26 50L50 30M36 42L52 70" stroke="url(#grad)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M58 30L70 70L82 30" stroke="url(#grad)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <defs>
    <linearGradient id="grad" x1="0" y1="0" x2="100" y2="100" gradientUnits="userSpaceOnUse">
      <stop stop-color="#3B82F6"/>
      <stop offset="0.5" stop-color="#8B5CF6"/>
      <stop offset="1" stop-color="#06B6D4"/>
    </linearGradient>
  </defs>
</svg>
""",

    "public/profile-placeholder.svg": r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" fill="none">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="400" y2="400" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0a0f24"/>
      <stop offset="50%" stop-color="#111a3a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="50" y1="50" x2="350" y2="350" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="50%" stop-color="#8b5cf6"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" rx="40" fill="url(#bgGrad)"/>
  <circle cx="200" cy="200" r="165" stroke="url(#accentGrad)" stroke-width="2" stroke-dasharray="8 8" opacity="0.4"/>
  <circle cx="200" cy="150" r="58" fill="url(#accentGrad)" opacity="0.85"/>
  <path d="M95 340C95 278 140 240 200 240C260 240 305 278 305 340" fill="url(#accentGrad)" opacity="0.85"/>
  <rect x="115" y="325" width="170" height="36" rx="18" fill="#050816" stroke="url(#accentGrad)" stroke-width="2"/>
  <text x="200" y="348" text-anchor="middle" fill="#e2e8f0" font-family="monospace" font-weight="bold" font-size="14">KURUBA VASU</text>
</svg>
""",

    "src/data/portfolioData.js": r"""export const personalInfo = {
  name: 'Kuruba Vasu',
  initials: 'KV',
  roles: [
    'Python Full Stack Developer',
    'Software Developer',
    'B.Tech CSE Student',
    'Django & React.js Developer',
  ],
  tagline: 'Python Full Stack Developer | Software Developer | B.Tech CSE Student',
  education: 'B.Tech Computer Science and Engineering',
  college: 'Dr. K.V. Subba Reddy Institute of Technology',
  location: 'Kurnool, Andhra Pradesh, India',
  cgpa: '8.76',
  careerGoal: 'To become a professional software developer.',
  bio: `I am a dedicated Computer Science and Engineering undergraduate at Dr. K.V. Subba Reddy Institute of Technology, Kurnool, holding a 8.76 CGPA. I specialize in architecting and building full-stack web applications using Python, Django, REST APIs, React.js, and MySQL. Passionate about clean code, scalable backend architecture, and intuitive user interfaces, my goal is to become a professional software developer solving impactful real-world engineering challenges.`,
  // Replace '/profile-placeholder.svg' with '/profile.jpg' after placing your photo in public/profile.jpg
  profilePhoto: '/profile.jpg',
  fallbackPhoto: '/profile-placeholder.svg',
  // Place your PDF in public/Kuruba_Vasu_Resume.pdf
  resumeUrl: '/Kuruba_Vasu_Resume.pdf',
  email: 'kurubavasu.dev@gmail.com',
  socials: {
    github: 'https://github.com/kurubavasu',
    linkedin: 'https://www.linkedin.com/in/kuruba-vasu',
    email: 'mailto:kurubavasu.dev@gmail.com',
  },
};

export const statsData = [
  {
    id: 1,
    label: 'B.Tech CGPA',
    value: 8.76,
    decimals: 2,
    suffix: ' / 10',
    description: 'Consistent academic excellence in CSE',
  },
  {
    id: 2,
    label: 'Featured Projects',
    value: 4,
    decimals: 0,
    suffix: '',
    description: 'Full-stack, AI & data analysis builds',
  },
  {
    id: 3,
    label: 'Technical Skills',
    value: 18,
    decimals: 0,
    suffix: '+',
    description: 'Languages, frameworks, tools & CS core',
  },
  {
    id: 4,
    label: 'Verified Certifications',
    value: 2,
    decimals: 0,
    suffix: '+',
    description: 'NPTEL AI & Ethical Hacking credentials',
  },
];

export const skillCategories = [
  'All',
  'Programming',
  'Frontend',
  'Backend',
  'Database',
  'Tools',
  'Core Subjects',
];

export const skillsData = [
  // Programming
  {
    name: 'Python',
    category: 'Programming',
    level: 92,
    badge: 'Primary Language',
    icon: 'Terminal',
    color: 'from-blue-500 to-cyan-400',
    description: 'Object-oriented programming, scripting, automation, backend web architecture, and AI integration.',
  },
  {
    name: 'JavaScript',
    category: 'Programming',
    level: 85,
    badge: 'ES6+',
    icon: 'Code2',
    color: 'from-amber-400 to-yellow-500',
    description: 'Asynchronous programming, DOM manipulation, modern ES6+ syntax, and interactive UI logic.',
  },
  {
    name: 'Java (Basics)',
    category: 'Programming',
    level: 70,
    badge: 'OOP Foundation',
    icon: 'Coffee',
    color: 'from-orange-500 to-red-500',
    description: 'Core object-oriented principles, class design, exception handling, and servlet fundamentals.',
  },

  // Frontend
  {
    name: 'HTML5',
    category: 'Frontend',
    level: 94,
    badge: 'Semantic Web',
    icon: 'Layout',
    color: 'from-orange-500 to-amber-500',
    description: 'Accessible, SEO-friendly semantic markup and modern document structure.',
  },
  {
    name: 'CSS3',
    category: 'Frontend',
    level: 90,
    badge: 'Responsive UI',
    icon: 'Palette',
    color: 'from-blue-500 to-indigo-500',
    description: 'Flexbox, CSS Grid, responsive media queries, glassmorphism, and keyframe animations.',
  },
  {
    name: 'React.js',
    category: 'Frontend',
    level: 84,
    badge: 'SPA Library',
    icon: 'Atom',
    color: 'from-cyan-400 to-blue-500',
    description: 'Component-driven architecture, React Hooks, state management, and REST API consumption.',
  },

  // Backend
  {
    name: 'Django',
    category: 'Backend',
    level: 88,
    badge: 'Python Framework',
    icon: 'Server',
    color: 'from-emerald-500 to-teal-500',
    description: 'MVT architecture, ORM modeling, authentication, admin customization, and secure backend logic.',
  },
  {
    name: 'REST APIs',
    category: 'Backend',
    level: 86,
    badge: 'API Design',
    icon: 'Webhook',
    color: 'from-violet-500 to-purple-500',
    description: 'JSON serialization, CRUD endpoints, token/session authentication, and frontend-backend integration.',
  },
  {
    name: 'Java Servlets',
    category: 'Backend',
    level: 72,
    badge: 'Server-Side Java',
    icon: 'Cpu',
    color: 'from-rose-500 to-orange-500',
    description: 'Request-response lifecycle, session management, and dynamic web application handling.',
  },

  // Database
  {
    name: 'MySQL',
    category: 'Database',
    level: 88,
    badge: 'RDBMS',
    icon: 'Database',
    color: 'from-sky-400 to-blue-600',
    description: 'Relational schema design, indexing, joins, stored queries, and Django/Python integration.',
  },
  {
    name: 'SQL',
    category: 'Database',
    level: 90,
    badge: 'Query Language',
    icon: 'Table',
    color: 'from-indigo-400 to-purple-600',
    description: 'DDL, DML, complex joins, aggregations, normalization, and data integrity constraints.',
  },

  // Tools
  {
    name: 'Git',
    category: 'Tools',
    level: 86,
    badge: 'Version Control',
    icon: 'GitBranch',
    color: 'from-orange-500 to-red-600',
    description: 'Branching workflows, commit hygiene, merge conflict resolution, and source tracking.',
  },
  {
    name: 'GitHub',
    category: 'Tools',
    level: 88,
    badge: 'Collaboration',
    icon: 'Github',
    color: 'from-slate-400 to-slate-200',
    description: 'Repository management, pull requests, project documentation, and code hosting.',
  },
  {
    name: 'VS Code',
    category: 'Tools',
    level: 92,
    badge: 'IDE',
    icon: 'Code',
    color: 'from-blue-400 to-blue-600',
    description: 'Debugging, extensions workflow, integrated terminal, and multi-language development.',
  },
  {
    name: 'Microsoft Excel',
    category: 'Tools',
    level: 85,
    badge: 'Data Analytics',
    icon: 'BarChart3',
    color: 'from-emerald-400 to-green-600',
    description: 'Pivot tables, dynamic charts, VLOOKUP/XLOOKUP, data cleaning, and interactive KPI dashboards.',
  },

  // Core Subjects
  {
    name: 'Data Structures & Algorithms',
    category: 'Core Subjects',
    level: 84,
    badge: 'Problem Solving',
    icon: 'Network',
    color: 'from-purple-500 to-pink-500',
    description: 'Arrays, linked lists, stacks, queues, trees, sorting, searching, and time-space complexity.',
  },
  {
    name: 'DBMS',
    category: 'Core Subjects',
    level: 88,
    badge: 'Core CS',
    icon: 'HardDrive',
    color: 'from-cyan-400 to-teal-500',
    description: 'ACID properties, ER modeling, relational algebra, normalization (1NF–BCNF), and transactions.',
  },
  {
    name: 'Operating Systems',
    category: 'Core Subjects',
    level: 82,
    badge: 'Core CS',
    icon: 'Layers',
    color: 'from-blue-500 to-purple-500',
    description: 'Process scheduling, multithreading, memory management, deadlocks, and file systems.',
  },
  {
    name: 'Computer Networks',
    category: 'Core Subjects',
    level: 82,
    badge: 'Core CS',
    icon: 'Globe',
    color: 'from-indigo-500 to-cyan-400',
    description: 'OSI & TCP/IP models, HTTP/HTTPS protocols, DNS, routing, and client-server communication.',
  },
];

export const projectsData = [
  {
    id: 'shopsphere',
    title: 'ShopSphere – Full Stack E-Commerce Web Application',
    category: 'Full Stack Web Application',
    shortDescription:
      'A comprehensive full-stack e-commerce web application engineered with a responsive storefront, product catalog management, shopping cart workflows, and relational database persistence.',
    architectureSummary:
      'Built using a modular full-stack architecture separating presentation components from backend business logic and relational database tables.',
    features: [
      'Dynamic product catalog with category filtering and search functionality',
      'User authentication, session management, and secure account workflows',
      'Interactive shopping cart state management and order checkout pipeline',
      'Relational database schema in MySQL managing products, users, and orders',
    ],
    technologies: ['Python', 'Django', 'React.js', 'JavaScript', 'HTML5', 'CSS3', 'MySQL', 'REST APIs'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-blue-500 via-indigo-500 to-purple-600',
  },
  {
    id: 'student-placement',
    title: 'Student Placement Management System',
    category: 'Enterprise Web System',
    shortDescription:
      'A centralized academic placement portal designed to streamline student profile management, eligibility filtering, placement drive tracking, and coordinator workflows.',
    architectureSummary:
      'Role-based web application connecting students and placement coordinators through structured SQL database records and clean backend controllers.',
    features: [
      'Student registration, academic record management, and resume profile storage',
      'Automated filtering of eligible candidates based on CGPA and branch criteria',
      'Placement drive announcements and application status tracking',
      'Structured MySQL relational schema ensuring data consistency and fast queries',
    ],
    technologies: ['Python', 'Django', 'HTML5', 'CSS3', 'JavaScript', 'MySQL', 'SQL'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-cyan-500 via-blue-500 to-indigo-600',
  },
  {
    id: 'call-centre-dashboard',
    title: 'Call Centre Data Analysis Dashboard using Microsoft Excel',
    category: 'Data Analytics & Visualization',
    shortDescription:
      'An interactive analytical dashboard built in Microsoft Excel to transform raw call centre records into actionable performance insights, KPI summaries, and visual trend reports.',
    architectureSummary:
      'End-to-end spreadsheet data pipeline utilizing data cleaning, Pivot Tables, dynamic slicers, and custom visualization charts.',
    features: [
      'Data cleaning, normalization, and structured formatting of call log datasets',
      'Interactive Pivot Tables and multi-dimensional slicers for dynamic filtering',
      'Visual tracking of call volume trends, resolution metrics, and agent performance',
      'Executive summary layout designed for clear operational decision-making',
    ],
    technologies: ['Microsoft Excel', 'Pivot Tables', 'Data Cleaning', 'Data Visualization', 'Dashboard Design'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-emerald-500 via-teal-500 to-cyan-600',
  },
  {
    id: 'hey-vasu-ai',
    title: 'Hey Vasu – AI Voice Assistant',
    category: 'AI & Python Automation',
    shortDescription:
      'An intelligent Python-powered desktop voice assistant capable of recognizing spoken commands, synthesizing natural speech responses, and automating everyday system and web tasks.',
    architectureSummary:
      'Event-driven Python voice pipeline integrating speech-to-text recognition, command parsing, task execution modules, and text-to-speech synthesis.',
    features: [
      'Real-time voice wake-word and speech recognition command processing',
      'Natural text-to-speech audio feedback loop for conversational interaction',
      'Automated web searches, application launching, and information retrieval',
      'Modular Python command handler architecture for easy skill extensibility',
    ],
    technologies: ['Python', 'Speech Recognition', 'Text-to-Speech', 'Automation', 'APIs'],
    githubUrl: 'https://github.com/kurubavasu',
    liveUrl: null,
    accentColor: 'from-purple-500 via-fuchsia-500 to-pink-600',
  },
];

export const educationData = [
  {
    id: 'btech',
    degree: 'Bachelor of Technology (B.Tech) – Computer Science and Engineering',
    institution: 'Dr. K.V. Subba Reddy Institute of Technology',
    location: 'Kurnool, Andhra Pradesh, India',
    period: 'Pursuing (Undergraduate)',
    scoreLabel: 'CGPA',
    score: '8.76',
    highlights: [
      'Core focus on Software Engineering, Data Structures & Algorithms, DBMS, Operating Systems, and Computer Networks.',
      'Hands-on development of full-stack web applications using Python, Django, React.js, and MySQL.',
      'Active participant in technical certifications, coding labs, and software project exhibitions.',
    ],
  },
  {
    id: 'intermediate',
    degree: 'Intermediate Education (Class XII – MPC)',
    institution: 'Board of Intermediate Education, Andhra Pradesh',
    location: 'Andhra Pradesh, India',
    period: 'Completed',
    scoreLabel: 'Stream',
    score: 'Mathematics, Physics & Chemistry',
    highlights: [
      'Built strong analytical and mathematical foundations in calculus, algebra, and physical sciences.',
      'Developed logical problem-solving skills that transitioned directly into computer science fundamentals.',
    ],
  },
  {
    id: 'school',
    degree: 'Secondary School Education (SSC – Class X)',
    institution: 'Board of Secondary Education, Andhra Pradesh',
    location: 'Andhra Pradesh, India',
    period: 'Completed',
    scoreLabel: 'Foundation',
    score: 'General Sciences & Mathematics',
    highlights: [
      'Completed foundational schooling with strong academic discipline in mathematics, science, and computer literacy.',
    ],
  },
];

export const certificationsData = [
  {
    id: 'nptel-ai',
    title: 'NPTEL Fundamentals of AI',
    issuer: 'NPTEL (National Programme on Technology Enhanced Learning)',
    category: 'Artificial Intelligence',
    status: 'Verified Certification',
    skillsCovered: [
      'Intelligent Agents & Problem Solving',
      'Search Algorithms & Heuristics',
      'Knowledge Representation & Reasoning',
      'Foundations of Machine Intelligence',
    ],
    description:
      'Completed rigorous academic coursework covering the theoretical and algorithmic foundations of Artificial Intelligence through the NPTEL initiative.',
  },
  {
    id: 'ethical-hacking',
    title: 'Ethical Hacking Certification',
    issuer: 'Verified Technical Certification',
    category: 'Cybersecurity & Application Security',
    status: 'Verified Certification',
    skillsCovered: [
      'Network Security Fundamentals',
      'Web Application Vulnerability Awareness',
      'Reconnaissance & Security Assessment Concepts',
      'Defensive Coding & Secure Authentication Practices',
    ],
    description:
      'Trained in ethical hacking methodologies, system vulnerability assessment, network protocols, and secure web application development practices.',
  },
  {
    id: 'fullstack-python-cert',
    title: 'Python Full Stack & Database Development Training',
    issuer: 'Academic & Technical Skill Verification',
    category: 'Full Stack Software Engineering',
    status: 'Verified Competency',
    skillsCovered: [
      'Python Object-Oriented Programming',
      'Django Web Framework & REST APIs',
      'Relational Database Design with MySQL & SQL',
      'Frontend Development with HTML5, CSS3, JS & React.js',
    ],
    description:
      'Demonstrated practical proficiency across the full software development lifecycle through verified academic coursework and end-to-end project implementations.',
  },
];

export const experienceData = [
  {
    id: 'practical-dev',
    role: 'Full Stack Software Development (Project Engineering)',
    type: 'Practical Development Experience',
    organization: 'Self-Directed & Academic Engineering Projects',
    location: 'Kurnool, Andhra Pradesh',
    highlights: [
      'Architected and developed ShopSphere, a full-stack e-commerce web application integrating Python, Django, REST APIs, React.js, and MySQL.',
      'Engineered a Student Placement Management System with relational SQL schemas to automate candidate eligibility filtering and placement workflows.',
      'Built "Hey Vasu", a modular Python AI Voice Assistant leveraging speech recognition, text-to-speech synthesis, and task automation.',
      'Designed an interactive Call Centre Data Analysis Dashboard in Microsoft Excel utilizing Pivot Tables, dynamic slicers, and KPI visualizations.',
    ],
    technologies: ['Python', 'Django', 'React.js', 'REST APIs', 'MySQL', 'Git & GitHub', 'Microsoft Excel'],
  },
  {
    id: 'technical-training',
    role: 'Technical Training & Core Computer Science Labs',
    type: 'Technical Training',
    organization: 'Dr. K.V. Subba Reddy Institute of Technology',
    location: 'Kurnool, Andhra Pradesh',
    highlights: [
      'Completed intensive hands-on programming laboratories in Python, Java (Basics), Java Servlets, Data Structures & Algorithms, and Database Management Systems.',
      'Practiced database normalization, complex SQL joins, and backend server integration across structured semester engineering labs.',
      'Applied Git and GitHub version control workflows for source code management and technical documentation.',
    ],
    technologies: ['Python', 'Java (Basics)', 'Java Servlets', 'DSA', 'DBMS', 'SQL', 'OS & Networks'],
  },
  {
    id: 'internship-readiness',
    role: 'Software Engineering Internship & Applied Training',
    type: 'Internship & Career Readiness',
    organization: 'Academic & Industry Skill Development',
    location: 'Andhra Pradesh, India',
    highlights: [
      'Trained in Agile software development lifecycles, RESTful API design patterns, and responsive frontend development.',
      'Combined NPTEL Artificial Intelligence foundations and Ethical Hacking security principles to write cleaner, safer, and more maintainable code.',
      'Actively prepared for full-time Software Developer and Python Full Stack Engineer roles with a strong 8.76 CGPA academic track record.',
    ],
    technologies: ['Full Stack Web Dev', 'REST Architecture', 'Application Security', 'AI Fundamentals'],
  },
];
""",

    "src/utils/generateResume.js": r"""import {
  personalInfo,
  skillsData,
  projectsData,
  educationData,
  certificationsData,
} from '../data/portfolioData';

export async function handleResumeDownload() {
  try {
    const response = await fetch(personalInfo.resumeUrl, { method: 'HEAD' });
    const contentType = response.headers.get('content-type') || '';
    if (response.ok && contentType.includes('pdf')) {
      const link = document.createElement('a');
      link.href = personalInfo.resumeUrl;
      link.download = 'Kuruba_Vasu_Resume.pdf';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      return;
    }
  } catch {
    // Fallback to generating printable resume view if static PDF is not placed in /public yet
  }

  const groupedSkills = skillsData.reduce((acc, skill) => {
    if (!acc[skill.category]) acc[skill.category] = [];
    acc[skill.category].push(skill.name);
    return acc;
  }, {});

  const resumeWindow = window.open('', '_blank');
  if (!resumeWindow) return;

  const htmlContent = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>${personalInfo.name} - Resume</title>
      <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
          font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
          color: #0f172a;
          background: #f8fafc;
          padding: 32px 16px;
          line-height: 1.5;
        }
        .toolbar {
          max-width: 820px;
          margin: 0 auto 16px auto;
          display: flex;
          justify-content: space-between;
          align-items: center;
          background: #0f172a;
          color: #fff;
          padding: 12px 20px;
          border-radius: 10px;
        }
        .toolbar button {
          background: #3b82f6;
          color: #fff;
          border: none;
          padding: 8px 16px;
          border-radius: 6px;
          font-weight: 600;
          cursor: pointer;
        }
        .page {
          max-width: 820px;
          margin: 0 auto;
          background: #ffffff;
          padding: 40px 48px;
          border-radius: 8px;
          box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        }
        .header {
          border-bottom: 2px solid #1e293b;
          padding-bottom: 16px;
          margin-bottom: 20px;
        }
        .header h1 {
          font-size: 28px;
          letter-spacing: -0.5px;
          color: #0f172a;
        }
        .header .role {
          font-size: 15px;
          font-weight: 600;
          color: #2563eb;
          margin-top: 4px;
        }
        .header .meta {
          margin-top: 8px;
          font-size: 13px;
          color: #475569;
          display: flex;
          flex-wrap: wrap;
          gap: 14px;
        }
        section { margin-bottom: 18px; }
        h2 {
          font-size: 14px;
          text-transform: uppercase;
          letter-spacing: 1px;
          color: #1e293b;
          border-bottom: 1px solid #cbd5e1;
          padding-bottom: 4px;
          margin-bottom: 10px;
        }
        p, li { font-size: 13.5px; color: #334155; }
        .skills-grid {
          display: grid;
          grid-template-columns: 150px 1fr;
          row-gap: 6px;
          font-size: 13.5px;
        }
        .skill-cat { font-weight: 700; color: #0f172a; }
        .item { margin-bottom: 12px; }
        .item-header {
          display: flex;
          justify-content: space-between;
          font-weight: 700;
          font-size: 14px;
          color: #0f172a;
        }
        .item-sub {
          font-size: 13px;
          color: #2563eb;
          font-weight: 600;
          margin-bottom: 4px;
        }
        ul { padding-left: 18px; margin-top: 4px; }
        @media print {
          body { background: #fff; padding: 0; }
          .toolbar { display: none; }
          .page { box-shadow: none; padding: 10px 20px; }
        }
      </style>
    </head>
    <body>
      <div class="toolbar">
        <span><strong>${personalInfo.name}</strong> — Official Curriculum Vitae</span>
        <button onclick="window.print()">Save as PDF / Print</button>
      </div>
      <div class="page">
        <div class="header">
          <h1>${personalInfo.name}</h1>
          <div class="role">${personalInfo.tagline}</div>
          <div class="meta">
            <span>Location: ${personalInfo.location}</span>
            <span>Email: ${personalInfo.email}</span>
            <span>GitHub: ${personalInfo.socials.github}</span>
            <span>LinkedIn: ${personalInfo.socials.linkedin}</span>
          </div>
        </div>

        <section>
          <h2>Career Objective</h2>
          <p>${personalInfo.careerGoal} ${personalInfo.bio}</p>
        </section>

        <section>
          <h2>Education</h2>
          ${educationData
            .map(
              (edu) => `
            <div class="item">
              <div class="item-header">
                <span>${edu.degree}</span>
                <span>${edu.scoreLabel}: ${edu.score}</span>
              </div>
              <div class="item-sub">${edu.institution} — ${edu.location}</div>
            </div>
          `
            )
            .join('')}
        </section>

        <section>
          <h2>Technical Skills</h2>
          <div class="skills-grid">
            ${Object.entries(groupedSkills)
              .map(
                ([cat, list]) => `
              <div class="skill-cat">${cat}:</div>
              <div>${list.join(', ')}</div>
            `
              )
              .join('')}
          </div>
        </section>

        <section>
          <h2>Technical Projects</h2>
          ${projectsData
            .map(
              (proj) => `
            <div class="item">
              <div class="item-header">
                <span>${proj.title}</span>
                <span>${proj.category}</span>
              </div>
              <div class="item-sub">Technologies: ${proj.technologies.join(', ')}</div>
              <p>${proj.shortDescription}</p>
              <ul>
                ${proj.features.map((f) => `<li>${f}</li>`).join('')}
              </ul>
            </div>
          `
            )
            .join('')}
        </section>

        <section>
          <h2>Certifications</h2>
          <ul>
            ${certificationsData
              .map(
                (cert) =>
                  `<li><strong>${cert.title}</strong> (${cert.issuer}) — ${cert.description}</li>`
              )
              .join('')}
          </ul>
        </section>
      </div>
    </body>
    </html>
  `;

  resumeWindow.document.open();
  resumeWindow.document.write(htmlContent);
  resumeWindow.document.close();
}
""",

    "src/index.css": r"""@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --bg-primary: #f8fafc;
    --bg-secondary: #ffffff;
    --text-primary: #0f172a;
    --text-secondary: #475569;
  }

  .dark {
    --bg-primary: #050816;
    --bg-secondary: #0a0f24;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
  }

  html {
    scroll-behavior: smooth;
    scroll-padding-top: 5rem;
  }

  body {
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    transition: background-color 0.3s ease, color 0.3s ease;
  }
}

::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #050816;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #3b82f6, #8b5cf6);
  border-radius: 9999px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #60a5fa, #a78bfa);
}

@layer components {
  .glass-card {
    @apply bg-white/80 dark:bg-[#0d132a]/70 backdrop-blur-xl border border-slate-200/80 dark:border-white/10 shadow-xl dark:shadow-[0_8px_32px_0_rgba(0,0,0,0.37)];
  }

  .glass-pill {
    @apply bg-slate-100/90 dark:bg-white/[0.06] backdrop-blur-md border border-slate-200/80 dark:border-white/10;
  }

  .text-gradient {
    @apply bg-clip-text text-transparent bg-gradient-to-r from-blue-500 via-purple-500 to-cyan-400;
  }

  .btn-primary {
    @apply relative inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-semibold text-white bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 hover:from-blue-500 hover:via-indigo-500 hover:to-purple-500 shadow-lg shadow-blue-500/25 hover:shadow-blue-500/40 transition-all duration-300 active:scale-[0.98];
  }

  .btn-secondary {
    @apply inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-semibold text-slate-800 dark:text-slate-100 bg-white/90 dark:bg-white/[0.06] hover:bg-slate-100 dark:hover:bg-white/[0.12] border border-slate-300 dark:border-white/15 backdrop-blur-md transition-all duration-300 active:scale-[0.98];
  }
}

.bg-grid-pattern {
  background-size: 42px 42px;
  background-image: 
    linear-gradient(to right, rgba(148, 163, 184, 0.06) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(148, 163, 184, 0.06) 1px, transparent 1px);
}
""",

    "src/components/Loader.jsx": r"""import React, { useEffect, useState } from 'react';
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
""",

    "src/components/CustomCursor.jsx": r"""import React, { useEffect, useState } from 'react';
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
""",

    "src/components/ParticleBackground.jsx": r"""import React, { useEffect, useRef } from 'react';

export default function ParticleBackground({ isDark }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animationFrameId;

    const setCanvasSize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    setCanvasSize();
    window.addEventListener('resize', setCanvasSize);

    const particleCount = Math.min(45, Math.floor(window.innerWidth / 32));
    const particles = Array.from({ length: particleCount }, () => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      radius: Math.random() * 1.8 + 0.7,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      alpha: Math.random() * 0.5 + 0.2,
    }));

    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = isDark
          ? `rgba(96, 165, 250, ${p.alpha})`
          : `rgba(59, 130, 246, ${p.alpha * 0.6})`;
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dx = p.x - p2.x;
          const dy = p.y - p2.y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 130) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            const lineAlpha = (1 - dist / 130) * (isDark ? 0.14 : 0.08);
            ctx.strokeStyle = `rgba(139, 92, 246, ${lineAlpha})`;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }
      }

      animationFrameId = requestAnimationFrame(draw);
    };

    draw();

    return () => {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener('resize', setCanvasSize);
    };
  }, [isDark]);

  return (
    <canvas
      ref={canvasRef}
      className="fixed inset-0 pointer-events-none z-0 opacity-80"
      aria-hidden="true"
    />
  );
}
""",

    "src/components/TiltCard.jsx": r"""import React, { useState } from 'react';
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
""",

    "src/components/SectionHeading.jsx": r"""import React from 'react';
import { motion } from 'framer-motion';

export default function SectionHeading({ badge, title, highlight, subtitle }) {
  return (
    <div className="text-center max-w-3xl mx-auto mb-14 sm:mb-16">
      <motion.div
        initial={{ opacity: 0, y: 15 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.45 }}
        className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full glass-pill text-xs sm:text-sm font-mono font-medium text-blue-600 dark:text-blue-400 mb-4"
      >
        <span className="w-2 h-2 rounded-full bg-gradient-to-r from-blue-500 to-purple-500 animate-pulse" />
        <span>{badge}</span>
      </motion.div>

      <motion.h2
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.3 }}
        transition={{ duration: 0.5, delay: 0.08 }}
        className="font-display text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900 dark:text-white mb-4"
      >
        {title}{' '}
        {highlight && <span className="text-gradient">{highlight}</span>}
      </motion.h2>

      {subtitle && (
        <motion.p
          initial={{ opacity: 0, y: 18 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.5, delay: 0.15 }}
          className="text-slate-600 dark:text-slate-400 text-base sm:text-lg leading-relaxed"
        >
          {subtitle}
        </motion.p>
      )}
    </div>
  );
}
""",

    "src/components/Navbar.jsx": r"""import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Menu,
  X,
  Sun,
  Moon,
  Download,
  Code2,
  ChevronRight,
} from 'lucide-react';
import { personalInfo } from '../data/portfolioData';
import { handleResumeDownload } from '../utils/generateResume';

const navLinks = [
  { name: 'Home', href: '#home' },
  { name: 'About', href: '#about' },
  { name: 'Skills', href: '#skills' },
  { name: 'Projects', href: '#projects' },
  { name: 'Education', href: '#education' },
  { name: 'Certifications', href: '#certifications' },
  { name: 'Experience', href: '#experience' },
  { name: 'Contact', href: '#contact' },
];

export default function Navbar({ isDark, toggleTheme }) {
  const [scrolled, setScrolled] = useState(false);
  const [activeSection, setActiveSection] = useState('home');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 24);

      const sections = navLinks.map((link) => link.href.substring(1));
      const scrollPosition = window.scrollY + 180;

      for (const sectionId of sections) {
        const el = document.getElementById(sectionId);
        if (el) {
          const top = el.offsetTop;
          const height = el.offsetHeight;
          if (scrollPosition >= top && scrollPosition < top + height) {
            setActiveSection(sectionId);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNavClick = (e, href) => {
    e.preventDefault();
    setMobileMenuOpen(false);
    const target = document.querySelector(href);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-40 transition-all duration-300 ${
        scrolled
          ? 'py-3 bg-white/85 dark:bg-[#050816]/85 backdrop-blur-xl border-b border-slate-200/80 dark:border-white/10 shadow-lg shadow-black/5'
          : 'py-5 bg-transparent'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
        <a
          href="#home"
          onClick={(e) => handleNavClick(e, '#home')}
          className="flex items-center gap-3 group focus:outline-none"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-600 flex items-center justify-center text-white font-display font-bold text-lg shadow-md shadow-blue-500/25 group-hover:scale-105 transition-transform">
            {personalInfo.initials}
          </div>
          <div className="flex flex-col">
            <span className="font-display font-bold text-base sm:text-lg tracking-tight text-slate-900 dark:text-white leading-none">
              {personalInfo.name}
            </span>
            <span className="font-mono text-[11px] text-blue-600 dark:text-blue-400 mt-0.5 flex items-center gap-1">
              <Code2 className="w-3 h-3" /> Full Stack Dev
            </span>
          </div>
        </a>

        <nav className="hidden xl:flex items-center gap-1 p-1.5 rounded-2xl glass-pill">
          {navLinks.map((link) => {
            const isActive = activeSection === link.href.substring(1);
            return (
              <a
                key={link.name}
                href={link.href}
                onClick={(e) => handleNavClick(e, link.href)}
                className={`relative px-3.5 py-2 rounded-xl text-sm font-medium transition-colors ${
                  isActive
                    ? 'text-white'
                    : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                {isActive && (
                  <motion.span
                    layoutId="activeNavIndicator"
                    className="absolute inset-0 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 -z-10 shadow-md shadow-blue-500/25"
                    transition={{ type: 'spring', stiffness: 350, damping: 30 }}
                  />
                )}
                {link.name}
              </a>
            );
          })}
        </nav>

        <div className="flex items-center gap-2.5">
          <button
            onClick={toggleTheme}
            aria-label="Toggle Dark/Light Theme"
            className="p-2.5 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:border-blue-500/50 transition-all"
            title={isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
          >
            {isDark ? (
              <Sun className="w-5 h-5 text-amber-400" />
            ) : (
              <Moon className="w-5 h-5 text-indigo-600" />
            )}
          </button>

          <button
            onClick={handleResumeDownload}
            className="hidden sm:inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 shadow-md shadow-blue-500/20 transition-all"
          >
            <Download className="w-4 h-4" />
            <span>Resume</span>
          </button>

          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle Navigation Menu"
            className="xl:hidden p-2.5 rounded-xl glass-pill text-slate-800 dark:text-slate-100"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.25 }}
            className="xl:hidden overflow-hidden bg-white/95 dark:bg-[#080d21]/95 backdrop-blur-2xl border-b border-slate-200 dark:border-white/10"
          >
            <div className="max-w-7xl mx-auto px-4 py-5 flex flex-col gap-2">
              {navLinks.map((link) => {
                const isActive = activeSection === link.href.substring(1);
                return (
                  <a
                    key={link.name}
                    href={link.href}
                    onClick={(e) => handleNavClick(e, link.href)}
                    className={`flex items-center justify-between px-4 py-3 rounded-xl font-medium text-sm transition-all ${
                      isActive
                        ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-md'
                        : 'text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-white/5'
                    }`}
                  >
                    <span>{link.name}</span>
                    <ChevronRight className="w-4 h-4 opacity-75" />
                  </a>
                );
              })}

              <button
                onClick={() => {
                  setMobileMenuOpen(false);
                  handleResumeDownload();
                }}
                className="mt-2 w-full btn-primary text-sm py-3"
              >
                <Download className="w-4 h-4" />
                <span>Download Resume</span>
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
""",

    "src/components/Hero.jsx": r"""import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import {
  Download,
  ArrowRight,
  Github,
  Linkedin,
  Mail,
  MapPin,
  Sparkles,
  GraduationCap,
  Terminal,
  Database,
  Code2,
} from 'lucide-react';
import { personalInfo } from '../data/portfolioData';
import { handleResumeDownload } from '../utils/generateResume';
import TiltCard from './TiltCard';

export default function Hero() {
  const [roleIndex, setRoleIndex] = useState(0);
  const [displayText, setDisplayText] = useState('');
  const [isDeleting, setIsDeleting] = useState(false);
  const [imgSrc, setImgSrc] = useState(personalInfo.profilePhoto);

  useEffect(() => {
    const currentRole = personalInfo.roles[roleIndex];
    const typingSpeed = isDeleting ? 45 : 90;

    const timer = setTimeout(() => {
      if (!isDeleting && displayText === currentRole) {
        setTimeout(() => setIsDeleting(true), 1600);
      } else if (isDeleting && displayText === '') {
        setIsDeleting(false);
        setRoleIndex((prev) => (prev + 1) % personalInfo.roles.length);
      } else {
        setDisplayText(
          currentRole.substring(
            0,
            displayText.length + (isDeleting ? -1 : 1)
          )
        );
      }
    }, typingSpeed);

    return () => clearTimeout(timer);
  }, [displayText, isDeleting, roleIndex]);

  const scrollToProjects = (e) => {
    e.preventDefault();
    const el = document.getElementById('projects');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section
      id="home"
      className="relative min-h-screen flex items-center pt-28 pb-20 overflow-hidden bg-grid-pattern"
    >
      <div className="pointer-events-none absolute -top-24 -left-24 w-96 h-96 rounded-full bg-blue-600/20 dark:bg-blue-600/25 blur-[130px] animate-pulse-slow" />
      <div className="pointer-events-none absolute top-1/3 -right-24 w-[28rem] h-[28rem] rounded-full bg-purple-600/20 dark:bg-purple-600/25 blur-[140px] animate-pulse-slow" />
      <div className="pointer-events-none absolute bottom-0 left-1/3 w-80 h-80 rounded-full bg-cyan-500/15 blur-[120px]" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          <div className="lg:col-span-7 text-center lg:text-left">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
              className="inline-flex items-center gap-2.5 px-4 py-2 rounded-full glass-pill mb-6"
            >
              <span className="relative flex h-2.5 w-2.5">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75" />
                <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500" />
              </span>
              <span className="text-xs sm:text-sm font-medium text-slate-700 dark:text-slate-200">
                Open to Software Developer & Full Stack Opportunities
              </span>
            </motion.div>

            <motion.h1
              initial={{ opacity: 0, y: 24 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.1 }}
              className="font-display text-4xl sm:text-5xl xl:text-6xl font-extrabold tracking-tight text-slate-900 dark:text-white leading-[1.12] mb-4"
            >
              Hi, I&apos;m{' '}
              <span className="text-gradient">Kuruba Vasu</span>
            </motion.h1>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.2 }}
              className="h-10 sm:h-12 flex items-center justify-center lg:justify-start mb-5"
            >
              <span className="font-mono text-lg sm:text-2xl lg:text-3xl font-semibold text-blue-600 dark:text-blue-400">
                &gt; {displayText}
                <span className="inline-block w-2.5 h-6 sm:h-7 ml-1 bg-purple-500 animate-pulse align-middle" />
              </span>
            </motion.div>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.3 }}
              className="text-slate-600 dark:text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl mx-auto lg:mx-0 mb-6"
            >
              B.Tech Computer Science &amp; Engineering student at{' '}
              <span className="font-semibold text-slate-900 dark:text-white">
                {personalInfo.college}
              </span>{' '}
              (CGPA: <span className="text-blue-500 font-bold">{personalInfo.cgpa}</span>). Passionate about building scalable web applications with{' '}
              <span className="text-slate-900 dark:text-white font-medium">
                Python, Django, REST APIs, React.js, and MySQL
              </span>
              .
            </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.35 }}
              className="flex flex-wrap items-center justify-center lg:justify-start gap-3 mb-8 text-xs sm:text-sm text-slate-600 dark:text-slate-400"
            >
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl glass-pill">
                <MapPin className="w-4 h-4 text-blue-500" />
                {personalInfo.location}
              </span>
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl glass-pill">
                <GraduationCap className="w-4 h-4 text-purple-500" />
                B.Tech CSE • CGPA {personalInfo.cgpa}
              </span>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.42 }}
              className="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 mb-9"
            >
              <button
                onClick={handleResumeDownload}
                className="w-full sm:w-auto btn-primary group"
              >
                <Download className="w-5 h-5 group-hover:-translate-y-0.5 transition-transform" />
                <span>Download Resume</span>
              </button>

              <a
                href="#projects"
                onClick={scrollToProjects}
                className="w-full sm:w-auto btn-secondary group"
              >
                <span>Explore My Work</span>
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform text-blue-500" />
              </a>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.55, delay: 0.5 }}
              className="flex items-center justify-center lg:justify-start gap-4"
            >
              <span className="text-xs font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400">
                Connect:
              </span>
              <a
                href={personalInfo.socials.github}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="GitHub Profile"
                className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:text-white hover:bg-blue-600 dark:hover:bg-blue-600 hover:border-blue-500 transition-all hover:-translate-y-1"
              >
                <Github className="w-5 h-5" />
              </a>
              <a
                href={personalInfo.socials.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="LinkedIn Profile"
                className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:text-white hover:bg-blue-600 dark:hover:bg-blue-600 hover:border-blue-500 transition-all hover:-translate-y-1"
              >
                <Linkedin className="w-5 h-5" />
              </a>
              <a
                href={personalInfo.socials.email}
                aria-label="Send Email"
                className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-200 hover:text-white hover:bg-purple-600 dark:hover:bg-purple-600 hover:border-purple-500 transition-all hover:-translate-y-1"
              >
                <Mail className="w-5 h-5" />
              </a>
            </motion.div>
          </div>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.65, delay: 0.25 }}
            className="lg:col-span-5 flex justify-center"
          >
            <div className="relative w-full max-w-sm sm:max-w-md">
              <div className="absolute -inset-2 rounded-[2.2rem] bg-gradient-to-r from-blue-500 via-purple-500 to-cyan-400 opacity-35 blur-xl animate-pulse-slow" />

              <TiltCard className="glass-card rounded-[2rem] p-6 sm:p-7 relative">
                <div className="flex items-center justify-between pb-4 mb-5 border-b border-slate-200/70 dark:border-white/10">
                  <div className="flex items-center gap-2">
                    <span className="w-3 h-3 rounded-full bg-rose-500" />
                    <span className="w-3 h-3 rounded-full bg-amber-400" />
                    <span className="w-3 h-3 rounded-full bg-emerald-500" />
                  </div>
                  <span className="font-mono text-xs text-slate-500 dark:text-slate-400">
                    kuruba_vasu.py
                  </span>
                  <Sparkles className="w-4 h-4 text-blue-400" />
                </div>

                <div className="relative mx-auto w-56 h-56 sm:w-64 sm:h-64 rounded-2xl overflow-hidden border-2 border-blue-500/30 shadow-2xl mb-6 bg-[#0a0f24] group">
                  <img
                    src={imgSrc}
                    onError={() => setImgSrc(personalInfo.fallbackPhoto)}
                    alt={personalInfo.name}
                    className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#050816]/80 via-transparent to-transparent" />
                  <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between px-3 py-1.5 rounded-xl bg-black/60 backdrop-blur-md border border-white/15 text-xs text-white">
                    <span className="font-semibold">{personalInfo.name}</span>
                    <span className="font-mono text-cyan-400">CGPA {personalInfo.cgpa}</span>
                  </div>
                </div>

                <div className="grid grid-cols-3 gap-2.5 text-center">
                  <div className="p-2.5 rounded-xl glass-pill flex flex-col items-center gap-1">
                    <Terminal className="w-4 h-4 text-blue-500" />
                    <span className="text-xs font-semibold text-slate-800 dark:text-slate-200">
                      Python
                    </span>
                    <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400">
                      Django / API
                    </span>
                  </div>
                  <div className="p-2.5 rounded-xl glass-pill flex flex-col items-center gap-1">
                    <Code2 className="w-4 h-4 text-cyan-400" />
                    <span className="text-xs font-semibold text-slate-800 dark:text-slate-200">
                      React.js
                    </span>
                    <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400">
                      Frontend UI
                    </span>
                  </div>
                  <div className="p-2.5 rounded-xl glass-pill flex flex-col items-center gap-1">
                    <Database className="w-4 h-4 text-purple-400" />
                    <span className="text-xs font-semibold text-slate-800 dark:text-slate-200">
                      MySQL
                    </span>
                    <span className="text-[10px] font-mono text-slate-500 dark:text-slate-400">
                      Relational DB
                    </span>
                  </div>
                </div>
              </TiltCard>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
""",

    "src/components/About.jsx": r"""import React, { useEffect, useState, useRef } from 'react';
import { motion, useInView } from 'framer-motion';
import {
  UserCheck,
  GraduationCap,
  Target,
  MapPin,
  Award,
  Code,
} from 'lucide-react';
import { personalInfo, statsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

function AnimatedCounter({ value, decimals = 0, suffix = '' }) {
  const [count, setCount] = useState(0);
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, amount: 0.4 });

  useEffect(() => {
    if (!isInView) return;

    let start = 0;
    const duration = 1600;
    const startTime = performance.now();

    const updateCounter = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const currentVal = start + eased * (value - start);
      setCount(currentVal);

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      } else {
        setCount(value);
      }
    };

    requestAnimationFrame(updateCounter);
  }, [isInView, value]);

  return (
    <span ref={ref}>
      {count.toFixed(decimals)}
      {suffix}
    </span>
  );
}

export default function About() {
  return (
    <section id="about" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="01. ABOUT ME"
          title="Engineering Solutions with"
          highlight="Clean Code & Architecture"
          subtitle="A closer look at my academic background, technical philosophy, and software engineering career goals."
        />

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch mb-14">
          <motion.div
            initial={{ opacity: 0, x: -24 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.25 }}
            transition={{ duration: 0.55 }}
            className="lg:col-span-7 glass-card rounded-3xl p-7 sm:p-9 flex flex-col justify-between"
          >
            <div>
              <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-blue-500/10 border border-blue-500/20 text-blue-600 dark:text-blue-400 text-xs font-mono font-semibold mb-5">
                <UserCheck className="w-4 h-4" />
                <span>PROFESSIONAL INTRODUCTION</span>
              </div>

              <h3 className="font-display text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white mb-4">
                Passionate Python Full Stack Developer from Kurnool, India
              </h3>

              <p className="text-slate-600 dark:text-slate-300 leading-relaxed mb-4 text-base">
                {personalInfo.bio}
              </p>

              <p className="text-slate-600 dark:text-slate-300 leading-relaxed text-base">
                Whether designing normalized relational database schemas in{' '}
                <strong className="text-slate-900 dark:text-white">MySQL</strong>, building RESTful backend workflows in{' '}
                <strong className="text-slate-900 dark:text-white">Python &amp; Django</strong>, or crafting interactive user interfaces in{' '}
                <strong className="text-slate-900 dark:text-white">React.js &amp; JavaScript</strong>, I focus on reliability, maintainability, and seamless user experience.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-6 mt-6 border-t border-slate-200/80 dark:border-white/10">
              <div className="flex items-start gap-3">
                <div className="p-2.5 rounded-xl bg-blue-500/10 text-blue-500 mt-0.5">
                  <MapPin className="w-5 h-5" />
                </div>
                <div>
                  <div className="text-xs font-mono uppercase text-slate-400">
                    Location
                  </div>
                  <div className="text-sm font-semibold text-slate-900 dark:text-white">
                    {personalInfo.location}
                  </div>
                </div>
              </div>

              <div className="flex items-start gap-3">
                <div className="p-2.5 rounded-xl bg-purple-500/10 text-purple-500 mt-0.5">
                  <Code className="w-5 h-5" />
                </div>
                <div>
                  <div className="text-xs font-mono uppercase text-slate-400">
                    Core Focus
                  </div>
                  <div className="text-sm font-semibold text-slate-900 dark:text-white">
                    Python Full Stack &amp; Software Dev
                  </div>
                </div>
              </div>
            </div>
          </motion.div>

          <div className="lg:col-span-5 flex flex-col gap-6">
            <motion.div
              initial={{ opacity: 0, x: 24 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 0.55 }}
              className="glass-card rounded-3xl p-7 flex-1 relative overflow-hidden"
            >
              <div className="absolute -right-8 -top-8 w-32 h-32 rounded-full bg-blue-500/10 blur-2xl pointer-events-none" />
              <div className="flex items-center gap-3 mb-4">
                <div className="p-3 rounded-2xl bg-gradient-to-br from-blue-500 to-indigo-600 text-white shadow-md shadow-blue-500/20">
                  <GraduationCap className="w-6 h-6" />
                </div>
                <div>
                  <span className="text-xs font-mono uppercase tracking-wider text-blue-500 font-semibold">
                    Academic Profile
                  </span>
                  <h4 className="font-display text-lg font-bold text-slate-900 dark:text-white">
                    {personalInfo.education}
                  </h4>
                </div>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-300 font-medium mb-3">
                {personalInfo.college}
              </p>
              <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-emerald-500/10 border border-emerald-500/25 text-emerald-600 dark:text-emerald-400 text-xs font-mono font-bold">
                <Award className="w-4 h-4" />
                <span>Current CGPA: {personalInfo.cgpa} / 10.0</span>
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 24 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 0.55, delay: 0.1 }}
              className="glass-card rounded-3xl p-7 flex-1 relative overflow-hidden"
            >
              <div className="absolute -right-8 -bottom-8 w-32 h-32 rounded-full bg-purple-500/10 blur-2xl pointer-events-none" />
              <div className="flex items-center gap-3 mb-4">
                <div className="p-3 rounded-2xl bg-gradient-to-br from-purple-500 to-pink-600 text-white shadow-md shadow-purple-500/20">
                  <Target className="w-6 h-6" />
                </div>
                <div>
                  <span className="text-xs font-mono uppercase tracking-wider text-purple-500 font-semibold">
                    Career Objective
                  </span>
                  <h4 className="font-display text-lg font-bold text-slate-900 dark:text-white">
                    {personalInfo.careerGoal}
                  </h4>
                </div>
              </div>
              <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
                Committed to contributing high-quality full-stack code, collaborating with agile engineering teams, and continuously advancing in modern software architecture.
              </p>
            </motion.div>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {statsData.map((stat, idx) => (
            <motion.div
              key={stat.id}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.45, delay: idx * 0.08 }}
            >
              <TiltCard className="glass-card rounded-2xl p-6 text-center h-full border-t-2 border-t-blue-500/40">
                <div className="font-display text-3xl sm:text-4xl font-extrabold text-gradient mb-1.5">
                  <AnimatedCounter
                    value={stat.value}
                    decimals={stat.decimals}
                    suffix={stat.suffix}
                  />
                </div>
                <div className="font-semibold text-slate-900 dark:text-white text-sm sm:text-base mb-1">
                  {stat.label}
                </div>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  {stat.description}
                </p>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
""",

    "src/components/Skills.jsx": r"""import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Terminal,
  Code2,
  Coffee,
  Layout,
  Palette,
  Atom,
  Server,
  Webhook,
  Cpu,
  Database,
  Table,
  GitBranch,
  Github,
  Code,
  BarChart3,
  Network,
  HardDrive,
  Layers,
  Globe,
} from 'lucide-react';
import { skillCategories, skillsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

const iconMap = {
  Terminal,
  Code2,
  Coffee,
  Layout,
  Palette,
  Atom,
  Server,
  Webhook,
  Cpu,
  Database,
  Table,
  GitBranch,
  Github,
  Code,
  BarChart3,
  Network,
  HardDrive,
  Layers,
  Globe,
};

export default function Skills() {
  const [selectedCategory, setSelectedCategory] = useState('All');

  const filteredSkills =
    selectedCategory === 'All'
      ? skillsData
      : skillsData.filter((s) => s.category === selectedCategory);

  return (
    <section id="skills" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="02. TECHNICAL ARSENAL"
          title="Skills, Technologies &"
          highlight="CS Foundations"
          subtitle="Comprehensive proficiency across full-stack development, relational databases, developer tooling, and core computer science subjects."
        />

        <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-12">
          {skillCategories.map((category) => {
            const isActive = selectedCategory === category;
            return (
              <button
                key={category}
                onClick={() => setSelectedCategory(category)}
                className={`relative px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                  isActive
                    ? 'text-white shadow-lg shadow-blue-500/25'
                    : 'glass-pill text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                {isActive && (
                  <motion.span
                    layoutId="activeSkillCategory"
                    className="absolute inset-0 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 -z-10"
                    transition={{ type: 'spring', stiffness: 350, damping: 28 }}
                  />
                )}
                {category}
              </button>
            );
          })}
        </div>

        <motion.div
          layout
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          <AnimatePresence mode="popLayout">
            {filteredSkills.map((skill) => {
              const IconComponent = iconMap[skill.icon] || Code2;
              return (
                <motion.div
                  key={skill.name}
                  layout
                  initial={{ opacity: 0, scale: 0.92 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.3 }}
                >
                  <TiltCard className="glass-card rounded-2xl p-6 h-full flex flex-col justify-between group hover:border-blue-500/40 transition-colors">
                    <div>
                      <div className="flex items-start justify-between gap-3 mb-4">
                        <div className="flex items-center gap-3.5">
                          <div
                            className={`p-3 rounded-xl bg-gradient-to-br ${skill.color} text-white shadow-md group-hover:scale-110 transition-transform`}
                          >
                            <IconComponent className="w-5 h-5" />
                          </div>
                          <div>
                            <h3 className="font-display font-bold text-lg text-slate-900 dark:text-white">
                              {skill.name}
                            </h3>
                            <span className="text-xs font-mono text-slate-500 dark:text-slate-400">
                              {skill.category}
                            </span>
                          </div>
                        </div>

                        <span className="px-2.5 py-1 rounded-lg glass-pill text-[11px] font-mono font-semibold text-blue-600 dark:text-blue-400">
                          {skill.badge}
                        </span>
                      </div>

                      <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-5">
                        {skill.description}
                      </p>
                    </div>

                    <div>
                      <div className="flex justify-between items-center text-xs font-mono mb-1.5">
                        <span className="text-slate-500 dark:text-slate-400">
                          Proficiency
                        </span>
                        <span className="font-bold text-slate-800 dark:text-slate-200">
                          {skill.level}%
                        </span>
                      </div>
                      <div className="w-full h-2 rounded-full bg-slate-200 dark:bg-white/10 overflow-hidden">
                        <motion.div
                          initial={{ width: 0 }}
                          whileInView={{ width: `${skill.level}%` }}
                          viewport={{ once: true }}
                          transition={{ duration: 1, ease: 'easeOut' }}
                          className={`h-full rounded-full bg-gradient-to-r ${skill.color}`}
                        />
                      </div>
                    </div>
                  </TiltCard>
                </motion.div>
              );
            })}
          </AnimatePresence>
        </motion.div>
      </div>
    </section>
  );
}
""",

    "src/components/Projects.jsx": r"""import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Github,
  ExternalLink,
  Layers,
  CheckCircle2,
  X,
  Code2,
  FolderGit2,
  Eye,
} from 'lucide-react';
import { projectsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

export default function Projects() {
  const [activeProjectModal, setActiveProjectModal] = useState(null);

  return (
    <section id="projects" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="03. FEATURED WORK"
          title="Software Engineering"
          highlight="Projects"
          subtitle="Real-world applications spanning full-stack web engineering, enterprise management portals, data analytics dashboards, and AI voice automation."
        />

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {projectsData.map((project, index) => (
            <motion.div
              key={project.id}
              initial={{ opacity: 0, y: 28 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <TiltCard className="glass-card rounded-3xl overflow-hidden h-full flex flex-col justify-between group border border-slate-200/80 dark:border-white/10 hover:border-blue-500/40 transition-all">
                <div>
                  <div
                    className={`relative h-48 sm:h-56 w-full bg-gradient-to-br ${project.accentColor} p-6 flex flex-col justify-between overflow-hidden`}
                  >
                    <div className="absolute inset-0 bg-black/25 backdrop-blur-[1px]" />
                    <div className="absolute -right-10 -bottom-10 w-44 h-44 rounded-full bg-white/10 blur-xl group-hover:scale-125 transition-transform duration-500" />

                    <div className="relative z-10 flex items-center justify-between">
                      <span className="px-3.5 py-1.5 rounded-full bg-black/40 backdrop-blur-md text-white text-xs font-mono font-medium border border-white/15">
                        {project.category}
                      </span>
                      <div className="p-2.5 rounded-xl bg-black/40 backdrop-blur-md text-white border border-white/15">
                        <FolderGit2 className="w-5 h-5" />
                      </div>
                    </div>

                    <div className="relative z-10">
                      <h3 className="font-display text-xl sm:text-2xl font-bold text-white leading-snug drop-shadow-sm">
                        {project.title}
                      </h3>
                    </div>
                  </div>

                  <div className="p-6 sm:p-8">
                    <p className="text-slate-600 dark:text-slate-300 text-sm sm:text-base leading-relaxed mb-5">
                      {project.shortDescription}
                    </p>

                    <div className="space-y-2 mb-6">
                      {project.features.slice(0, 3).map((feature, i) => (
                        <div
                          key={i}
                          className="flex items-start gap-2.5 text-xs sm:text-sm text-slate-600 dark:text-slate-300"
                        >
                          <CheckCircle2 className="w-4 h-4 text-blue-500 shrink-0 mt-0.5" />
                          <span>{feature}</span>
                        </div>
                      ))}
                    </div>

                    <div className="flex flex-wrap gap-2 mb-6">
                      {project.technologies.map((tech) => (
                        <span
                          key={tech}
                          className="px-3 py-1 rounded-lg glass-pill text-xs font-mono font-medium text-blue-600 dark:text-blue-300"
                        >
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="px-6 sm:px-8 pb-6 sm:pb-8 pt-4 border-t border-slate-200/70 dark:border-white/10 flex flex-wrap items-center gap-3">
                  <a
                    href={project.githubUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-slate-800 dark:text-white glass-pill hover:bg-slate-200/70 dark:hover:bg-white/15 transition-all"
                  >
                    <Github className="w-4 h-4" />
                    <span>GitHub Repository</span>
                  </a>

                  {project.liveUrl ? (
                    <a
                      href={project.liveUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 shadow-md shadow-blue-500/20 transition-all"
                    >
                      <ExternalLink className="w-4 h-4" />
                      <span>Live Demo</span>
                    </a>
                  ) : (
                    <button
                      onClick={() => setActiveProjectModal(project)}
                      className="flex-1 inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 shadow-md shadow-blue-500/20 transition-all"
                    >
                      <Eye className="w-4 h-4" />
                      <span>Interactive Overview</span>
                    </button>
                  )}
                </div>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>

      <AnimatePresence>
        {activeProjectModal && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setActiveProjectModal(null)}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md"
          >
            <motion.div
              initial={{ scale: 0.92, opacity: 0, y: 20 }}
              animate={{ scale: 1, opacity: 1, y: 0 }}
              exit={{ scale: 0.92, opacity: 0, y: 20 }}
              onClick={(e) => e.stopPropagation()}
              className="glass-card rounded-3xl max-w-2xl w-full overflow-hidden border border-white/20 shadow-2xl"
            >
              <div
                className={`p-6 sm:p-8 bg-gradient-to-r ${activeProjectModal.accentColor} text-white flex items-start justify-between gap-4`}
              >
                <div>
                  <span className="inline-block px-3 py-1 rounded-full bg-black/30 text-xs font-mono mb-2">
                    {activeProjectModal.category}
                  </span>
                  <h3 className="font-display text-2xl font-bold">
                    {activeProjectModal.title}
                  </h3>
                </div>
                <button
                  onClick={() => setActiveProjectModal(null)}
                  aria-label="Close Modal"
                  className="p-2 rounded-xl bg-black/30 hover:bg-black/50 text-white transition-colors"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <div className="p-6 sm:p-8 space-y-6 max-h-[75vh] overflow-y-auto">
                <div>
                  <h4 className="text-xs font-mono uppercase tracking-wider text-blue-500 font-semibold mb-2 flex items-center gap-1.5">
                    <Layers className="w-4 h-4" /> System Overview & Architecture
                  </h4>
                  <p className="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed mb-2">
                    {activeProjectModal.shortDescription}
                  </p>
                  <p className="text-sm text-slate-500 dark:text-slate-400 leading-relaxed">
                    {activeProjectModal.architectureSummary}
                  </p>
                </div>

                <div>
                  <h4 className="text-xs font-mono uppercase tracking-wider text-purple-500 font-semibold mb-3">
                    Key Technical Implementations
                  </h4>
                  <ul className="space-y-2.5">
                    {activeProjectModal.features.map((feat, idx) => (
                      <li
                        key={idx}
                        className="flex items-start gap-2.5 text-sm text-slate-700 dark:text-slate-200"
                      >
                        <CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0 mt-0.5" />
                        <span>{feat}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div>
                  <h4 className="text-xs font-mono uppercase tracking-wider text-cyan-500 font-semibold mb-3 flex items-center gap-1.5">
                    <Code2 className="w-4 h-4" /> Technologies Used
                  </h4>
                  <div className="flex flex-wrap gap-2">
                    {activeProjectModal.technologies.map((tech) => (
                      <span
                        key={tech}
                        className="px-3 py-1.5 rounded-xl glass-pill text-xs font-mono font-semibold text-blue-600 dark:text-blue-300"
                      >
                        {tech}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="pt-4 border-t border-slate-200 dark:border-white/10 flex flex-wrap items-center justify-end gap-3">
                  <a
                    href={activeProjectModal.githubUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn-primary text-sm py-2.5 px-5"
                  >
                    <Github className="w-4 h-4" />
                    <span>View on GitHub</span>
                  </a>
                  <button
                    onClick={() => setActiveProjectModal(null)}
                    className="btn-secondary text-sm py-2.5 px-5"
                  >
                    Close Preview
                  </button>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
""",

    "src/components/Education.jsx": r"""import React, { useEffect, useRef } from 'react';
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
""",

    "src/components/Certifications.jsx": r"""import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Award, ShieldCheck, CheckCircle2, Sparkles, X } from 'lucide-react';
import { certificationsData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

export default function Certifications() {
  const [selectedCert, setSelectedCert] = useState(null);

  return (
    <section id="certifications" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="05. CREDENTIALS"
          title="Verified"
          highlight="Certifications"
          subtitle="Continuous learning validated through NPTEL Artificial Intelligence coursework, Ethical Hacking certification, and full-stack technical training."
        />

        <div className="grid grid-cols-1 md:grid-cols-3 gap-7">
          {certificationsData.map((cert, index) => (
            <motion.div
              key={cert.id}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 0.45, delay: index * 0.1 }}
            >
              <TiltCard className="glass-card rounded-3xl p-7 h-full flex flex-col justify-between group border border-slate-200/80 dark:border-white/10 hover:border-purple-500/40 transition-all">
                <div>
                  <div className="flex items-center justify-between gap-2 mb-5">
                    <div className="p-3.5 rounded-2xl bg-gradient-to-br from-blue-600 via-indigo-600 to-purple-600 text-white shadow-lg shadow-blue-500/20 group-hover:scale-110 transition-transform">
                      <Award className="w-6 h-6" />
                    </div>
                    <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/25 text-emerald-600 dark:text-emerald-400 text-xs font-mono font-semibold">
                      <ShieldCheck className="w-3.5 h-3.5" />
                      {cert.status}
                    </span>
                  </div>

                  <span className="text-xs font-mono uppercase tracking-wider text-blue-600 dark:text-blue-400 font-semibold">
                    {cert.category}
                  </span>
                  <h3 className="font-display text-xl font-bold text-slate-900 dark:text-white mt-1 mb-2">
                    {cert.title}
                  </h3>
                  <p className="text-xs font-medium text-purple-600 dark:text-purple-400 mb-4">
                    Issued by: {cert.issuer}
                  </p>
                  <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-5">
                    {cert.description}
                  </p>
                </div>

                <div>
                  <div className="space-y-1.5 mb-6 pt-4 border-t border-slate-200/70 dark:border-white/10">
                    {cert.skillsCovered.slice(0, 3).map((skill, idx) => (
                      <div
                        key={idx}
                        className="flex items-center gap-2 text-xs text-slate-600 dark:text-slate-300"
                      >
                        <CheckCircle2 className="w-3.5 h-3.5 text-blue-500 shrink-0" />
                        <span>{skill}</span>
                      </div>
                    ))}
                  </div>

                  <button
                    onClick={() => setSelectedCert(cert)}
                    className="w-full py-2.5 px-4 rounded-xl glass-pill text-xs font-semibold text-slate-800 dark:text-white hover:bg-blue-600 hover:text-white dark:hover:bg-blue-600 transition-colors flex items-center justify-center gap-2"
                  >
                    <Sparkles className="w-4 h-4" />
                    <span>View Credential Details</span>
                  </button>
                </div>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>

      <AnimatePresence>
        {selectedCert && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedCert(null)}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md"
          >
            <motion.div
              initial={{ scale: 0.92, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.92, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
              className="glass-card rounded-3xl max-w-lg w-full p-6 sm:p-8 border border-white/20"
            >
              <div className="flex items-start justify-between gap-4 mb-5">
                <div className="flex items-center gap-3">
                  <div className="p-3 rounded-2xl bg-gradient-to-br from-blue-600 to-purple-600 text-white">
                    <Award className="w-6 h-6" />
                  </div>
                  <div>
                    <span className="text-xs font-mono text-emerald-400 font-semibold">
                      {selectedCert.status}
                    </span>
                    <h3 className="font-display text-xl font-bold text-slate-900 dark:text-white">
                      {selectedCert.title}
                    </h3>
                  </div>
                </div>
                <button
                  onClick={() => setSelectedCert(null)}
                  className="p-2 rounded-xl glass-pill text-slate-500 hover:text-white"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <p className="text-xs font-mono text-blue-500 mb-3">
                Issuer: {selectedCert.issuer}
              </p>
              <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-5">
                {selectedCert.description}
              </p>

              <h4 className="text-xs font-mono uppercase tracking-wider text-purple-500 font-semibold mb-3">
                Competencies & Topics Covered
              </h4>
              <ul className="space-y-2 mb-6">
                {selectedCert.skillsCovered.map((s, i) => (
                  <li
                    key={i}
                    className="flex items-center gap-2.5 text-sm text-slate-700 dark:text-slate-200"
                  >
                    <CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" />
                    <span>{s}</span>
                  </li>
                ))}
              </ul>

              <button
                onClick={() => setSelectedCert(null)}
                className="w-full btn-primary py-2.5 text-sm"
              >
                Close Details
              </button>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
""",

    "src/components/Experience.jsx": r"""import React from 'react';
import { motion } from 'framer-motion';
import { Briefcase, Terminal, CheckCircle2, MapPin } from 'lucide-react';
import { experienceData } from '../data/portfolioData';
import SectionHeading from './SectionHeading';
import TiltCard from './TiltCard';

export default function Experience() {
  return (
    <section id="experience" className="py-20 sm:py-28 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <SectionHeading
          badge="06. PRACTICAL EXPERIENCE"
          title="Development Experience &"
          highlight="Technical Training"
          subtitle="Hands-on software engineering experience across full-stack web builds, academic engineering laboratories, and industry-readiness training."
        />

        <div className="space-y-7">
          {experienceData.map((exp, index) => (
            <motion.div
              key={exp.id}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <TiltCard className="glass-card rounded-3xl p-6 sm:p-9 border-l-4 border-l-blue-500">
                <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-5 mb-5 border-b border-slate-200/80 dark:border-white/10">
                  <div className="flex items-start gap-4">
                    <div className="p-3.5 rounded-2xl bg-gradient-to-br from-blue-600 to-purple-600 text-white shadow-md shrink-0">
                      <Briefcase className="w-6 h-6" />
                    </div>
                    <div>
                      <span className="inline-block px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-600 dark:text-blue-400 text-xs font-mono font-semibold mb-1.5">
                        {exp.type}
                      </span>
                      <h3 className="font-display text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
                        {exp.role}
                      </h3>
                      <p className="text-sm font-medium text-slate-600 dark:text-slate-300 mt-0.5">
                        {exp.organization}
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-1.5 text-xs font-mono text-slate-500 dark:text-slate-400">
                    <MapPin className="w-4 h-4 text-purple-400" />
                    <span>{exp.location}</span>
                  </div>
                </div>

                <ul className="space-y-3 mb-6">
                  {exp.highlights.map((item, i) => (
                    <li
                      key={i}
                      className="flex items-start gap-3 text-sm sm:text-base text-slate-600 dark:text-slate-300"
                    >
                      <CheckCircle2 className="w-4 h-4 text-blue-500 shrink-0 mt-1" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>

                <div className="flex flex-wrap items-center gap-2 pt-2">
                  <span className="text-xs font-mono text-slate-400 flex items-center gap-1 mr-1">
                    <Terminal className="w-3.5 h-3.5 text-blue-400" /> Stack & Focus:
                  </span>
                  {exp.technologies.map((tech) => (
                    <span
                      key={tech}
                      className="px-3 py-1 rounded-lg glass-pill text-xs font-mono font-medium text-blue-600 dark:text-blue-300"
                    >
                      {tech}
                    </span>
                  ))}
                </div>
              </TiltCard>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
""",

    "src/components/Contact.jsx": r"""import React, { useState } from 'react';
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
""",

    "src/components/Footer.jsx": r"""import React from 'react';
import { Github, Linkedin, Mail, ArrowUp, Code2, Heart } from 'lucide-react';
import { personalInfo } from '../data/portfolioData';

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="relative border-t border-slate-200/80 dark:border-white/10 bg-white/60 dark:bg-[#040711]/90 backdrop-blur-xl py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-slate-200/70 dark:border-white/10">
          <div className="flex items-center gap-3.5 text-center md:text-left">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 to-purple-600 flex items-center justify-center text-white font-display font-bold text-lg shadow-md">
              {personalInfo.initials}
            </div>
            <div>
              <div className="font-display font-bold text-lg text-slate-900 dark:text-white">
                {personalInfo.name}
              </div>
              <div className="text-xs font-mono text-slate-500 dark:text-slate-400">
                {personalInfo.tagline}
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <a
              href={personalInfo.socials.github}
              target="_blank"
              rel="noopener noreferrer"
              aria-label="GitHub"
              className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-300 hover:text-white hover:bg-blue-600 transition-all"
            >
              <Github className="w-4 h-4" />
            </a>
            <a
              href={personalInfo.socials.linkedin}
              target="_blank"
              rel="noopener noreferrer"
              aria-label="LinkedIn"
              className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-300 hover:text-white hover:bg-blue-600 transition-all"
            >
              <Linkedin className="w-4 h-4" />
            </a>
            <a
              href={personalInfo.socials.email}
              aria-label="Email"
              className="p-3 rounded-xl glass-pill text-slate-700 dark:text-slate-300 hover:text-white hover:bg-purple-600 transition-all"
            >
              <Mail className="w-4 h-4" />
            </a>

            <button
              onClick={scrollToTop}
              aria-label="Back to top"
              className="ml-2 p-3 rounded-xl bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg shadow-blue-500/25 hover:-translate-y-1 transition-transform"
              title="Back to top"
            >
              <ArrowUp className="w-4 h-4" />
            </button>
          </div>
        </div>

        <div className="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500 dark:text-slate-400">
          <p>
            © {new Date().getFullYear()} <strong>{personalInfo.name}</strong>. All rights reserved.
          </p>
          <p className="flex items-center gap-1.5 font-mono">
            <Code2 className="w-4 h-4 text-blue-500" />
            <span>Built with React, Vite, Tailwind CSS, Framer Motion &amp; GSAP</span>
            <Heart className="w-3.5 h-3.5 text-rose-500 fill-rose-500" />
          </p>
        </div>
      </div>
    </footer>
  );
}
""",

    "src/App.jsx": r"""import React, { useState, useEffect } from 'react';
import { motion, useScroll, useSpring } from 'framer-motion';
import Loader from './components/Loader';
import CustomCursor from './components/CustomCursor';
import ParticleBackground from './components/ParticleBackground';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Skills from './components/Skills';
import Projects from './components/Projects';
import Education from './components/Education';
import Certifications from './components/Certifications';
import Experience from './components/Experience';
import Contact from './components/Contact';
import Footer from './components/Footer';

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [isDark, setIsDark] = useState(true);

  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 120,
    damping: 30,
    restDelta: 0.001,
  });

  useEffect(() => {
    const savedTheme = localStorage.getItem('kv_theme');
    if (savedTheme === 'light') {
      setIsDark(false);
      document.documentElement.classList.remove('dark');
    } else {
      setIsDark(true);
      document.documentElement.classList.add('dark');
    }
  }, []);

  const toggleTheme = () => {
    setIsDark((prev) => {
      const next = !prev;
      if (next) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('kv_theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('kv_theme', 'light');
      }
      return next;
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#050816] text-slate-900 dark:text-slate-100 relative selection:bg-blue-600 selection:text-white transition-colors duration-300">
      {isLoading && <Loader onComplete={() => setIsLoading(false)} />}

      <motion.div
        className="fixed top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-cyan-400 origin-left z-50"
        style={{ scaleX }}
      />

      <CustomCursor />
      <ParticleBackground isDark={isDark} />

      <Navbar isDark={isDark} toggleTheme={toggleTheme} />
      <main className="relative z-10">
        <Hero />
        <About />
        <Skills />
        <Projects />
        <Education />
        <Certifications />
        <Experience />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}
""",

    "src/main.jsx": r"""import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
""",

    "README.md": r"""# Kuruba Vasu — Personal Developer Portfolio

A modern, animated, full-stack developer portfolio website built for **Kuruba Vasu** (`Python Full Stack Developer | Software Developer | B.Tech CSE Student`).

## Quick Start in VS Code

```bash
npm install
npm run dev
```

## How to Replace Your Profile Photo & Resume

1. **Profile Photo:**
   - Place your photo inside the `public/` folder and name it `profile.jpg` (`public/profile.jpg`).
   - It will automatically display in the Hero card (and falls back to `/profile-placeholder.svg` if not added yet).

2. **Resume PDF:**
   - Place your PDF resume inside the `public/` folder and name it `Kuruba_Vasu_Resume.pdf` (`public/Kuruba_Vasu_Resume.pdf`).
   - Every **Download Resume** button will download this file (or open a printable CV generator if the file is not yet added).
"""
}


def extract_all():
    print("🚀 Extracting Kuruba Vasu Portfolio project files into current directory...")
    created_count = 0

    for filepath, content in FILES.items():
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.lstrip("\n"))

        created_count += 1
        print(f"  ✅ Created: {filepath}")

    print(f"\n🎉 Successfully extracted {created_count} files!")
    print("\n👉 Next steps in your VS Code Terminal:")
    print("   1. npm install")
    print("   2. npm run dev")


if __name__ == "__main__":
    extract_all()

 