
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Hermes Agent 中文生态",
  description: "让中文用户最快跑通 Hermes 的实战入口",
  themeConfig: {
    nav: [
      { text: '快速开始', link: '/guide/quickstart' },
      { text: '国内模型', link: '/providers/index' },
      { text: '多 Agent', link: '/multi-agent/index' },
      { text: 'Starter 模板', link: '/starters/index' },
      { text: 'Known Issues', link: '/known-issues/index' },
      { text: 'OpenClaw 迁移', link: '/openclaw/index' },
    ],
    sidebar: [
      {
        text: '入门指南',
        items: [
          { text: '什么是 Hermes', link: '/guide/what-is-hermes' },
          { text: '快速开始', link: '/guide/quickstart' },
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/zcweah1981/awesome-hermes-agent-zh' }
    ]
  }
})
