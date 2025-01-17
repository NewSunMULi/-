﻿using System;

namespace 化学卡牌_没有反应
{
    /// <summary>
    /// 存放着评级等级
    /// </summary>
    public enum 评级
    {
        Dog_H,
        Cxk_G,
        Bjk_Z,
        Apx_C
    }
    public static class Program
    {
        public static void Main(string[] args)
        {
            int score = 0;
            for (int i = 0; i<2; i++)
            {
                string[] 物质 = { "浓硫酸", "烷烃", "高锰酸钾[H+]", "烯烃", "炔烃", "芳香族化合物", "羧酸", "酯", "醇" };
                Console.WriteLine("你要出的物质！浓硫酸, 烷烃, 高锰酸钾[H+], 烯烃, 炔烃, 芳香族化合物, 羧酸, 酯, 醇");
                int player = Convert.ToInt32(Console.ReadLine());
                string plt = 物质[player];
                Random R = new Random();
                string robot = 物质[R.Next(0, 9)];
                if (((plt == "烯烃" || plt == "炔烃") && robot == "高锰酸钾[H+]") || ((robot == "烯烃" || robot == "炔烃") && plt == "高锰酸钾[H+]"))
                {
                    Console.WriteLine("你出的物质{0},人机出的物质{1}", plt, robot);
                    Console.WriteLine("发生反应，你寄了！");
                    score -= 1;
                }
                else if ((plt == "羧酸" && robot == "醇") || (plt == "醇" && robot == "羧酸"))
                {
                    Console.WriteLine("你出的物质{0},人机出的物质{1}", plt, robot);
                    Console.WriteLine("发生反应，你寄了！");
                    score -= 1;
                }
                else
                {
                    Console.WriteLine("你出的物质{0},人机出的物质{1}", plt, robot);
                    Console.WriteLine("算你运气好！");
                    score++;
                }
            }
            if (score <= 5)
            {
                Console.WriteLine("你就只得了这点屁分:{0},评级:{1}", score, 评级.Dog_H);
            }
            else if (score > 5 && score <= 10)
            {
                Console.WriteLine("你这得分有点少呀:{0},评级:{1}", score, 评级.Cxk_G);
            }
            else if (score <= 15 && score > 10)
            {
                Console.WriteLine("分数挺正常的:{0},评级:{1}", score, 评级.Bjk_Z);
            }
            else
            {
                Console.WriteLine("运气非常好，建议你下次那这些运气去抽波卡:{0},评级:{1}", score, 评级.Apx_C);
            }
            Console.WriteLine("点击任意键结束");
            Console.ReadKey();
        }
    }
}