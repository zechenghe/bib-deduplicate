# bib-deduplicate

This is a python script tool for cleaning up duplicated bib entries. I found it super useful while writing thesis -- because you have to merge several papers with debuplicated references.

#### Usage:
```
python bib-deduplicate --filename example.bib
```

#### Example (I used my own papers as examples :)):

example.bib:

```
@inproceedings{he2017secure,
  title={How secure is your cache against side-channel attacks?},
  author={He, Zecheng and Lee, Ruby B},
  booktitle={Proceedings of the 50th Annual IEEE/ACM International Symposium on Microarchitecture},
  pages={341--353},
  year={2017}
}

@inproceedings{he2019model,
  title={Model inversion attacks against collaborative inference},
  author={He, Zecheng and Zhang, Tianwei and Lee, Ruby B},
  booktitle={Proceedings of the 35th Annual Computer Security Applications Conference},
  pages={148--162},
  year={2019}
}

@inproceedings{he2019sensitive,
  title={Sensitive-sample fingerprinting of deep neural networks},
  author={He, Zecheng and Zhang, Tianwei and Lee, Ruby},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={4729--4737},
  year={2019}
}

@inproceedings{he2019model,
  title={Model inversion attacks against collaborative inference},
  author={He, Zecheng and Zhang, Tianwei and Lee, Ruby B},
  booktitle={Proceedings of the 35th Annual Computer Security Applications Conference},
  pages={148--162},
  year={2019}
}
```

#### Result

```
Remove duplicated he2019model
```

example_debup.bib:

```
@inproceedings{he2017secure,
  title={How secure is your cache against side-channel attacks?},
  author={He, Zecheng and Lee, Ruby B},
  booktitle={Proceedings of the 50th Annual IEEE/ACM International Symposium on Microarchitecture},
  pages={341--353},
  year={2017}
}

@inproceedings{he2019model,
  title={Model inversion attacks against collaborative inference},
  author={He, Zecheng and Zhang, Tianwei and Lee, Ruby B},
  booktitle={Proceedings of the 35th Annual Computer Security Applications Conference},
  pages={148--162},
  year={2019}
}

@inproceedings{he2019sensitive,
  title={Sensitive-sample fingerprinting of deep neural networks},
  author={He, Zecheng and Zhang, Tianwei and Lee, Ruby},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={4729--4737},
  year={2019}
}
```

example_dedup.bib can be directly used to generate pdf from tex.

#### TODO
Merge several bib files. Now you can simply achieve this by copying their content together and deduplicate.
