class IPIE {
public:
  virtual int getMaxPierniczkiCount(int count, int favorite[10][4],
                                    int available[4]) = 0;
};

class Judge {
public:
  static void run(IPIE *solution);
};