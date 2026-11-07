import {
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
