from typing import Generator, Iterable, Iterator, Sequence, Sized, Tuple, Union
from torch.utils.data import Sampler

class SizedSampler(Sized, Sampler):
  pass

class SizedIterator(Tuple, Iterator):
  pass

#class SizedGenerator(Sequence, Generator):
 # pass

class MySampler(Sampler):
  def __init__(self, sampler: Union[SizedIterator, SizedSampler]) -> None:
    self.sampler = sampler

  def __len__(self) -> int:
    return len(self.sampler)

